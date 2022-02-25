from conf.kp_conf import kp_conf
from conf.db_conf import db_conf
from utils.db_utils import DB_Utils
from kenpompy import utils
import pandas as pd
import numpy as np
from sqlalchemy import Integer, Float, Text

browser = utils.login(kp_conf["email"], kp_conf["password"])

def create_clean_joined_schedule(browser=browser,
                            joined_input_name=db_conf["raw_schedule_combined_tablename"],
                            load_from_schema=db_conf["staging_schema"],
                            clean_output_name=db_conf["clean_schedule_combined_tablename"],
                            save_to_schema=db_conf["staging_schema"],
                            if_exists="replace"
):
    """
    Function to take the clean schedule and join relevant features
    based on year and Team A/B

    Args:
        joined_input_name (str, optional): 
            Name of combined raw schedule table
            Defaults to db_conf["raw_schedule_combined_tablename"].
        load_from_schema (str, optional):
            Schema where combined raw schedule table exists
            Defaults to db_conf["staging_schema"]
        browser (optional):
            Should not need to edit this. Uses config kenpom credentials.
            Defaults to browser.
        clean_output_name (str, optional):
            Name of clean joined schedule to output to database
            Defaults to db_conf["clean_schedule_combined_tablename"]
        save_to_schema (str, optional):
            The schema to which the output table is saved
            Defaults to db_conf["staging_schema"]
        if_exists (str, optional):
            Follows if_exists from https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
            Defaults to "replace"

    Returns:
        None
    """    

    db_utils = DB_Utils()

    raw_schedule_cols_list = [
        "Season"
        , "Date"
        , "Location"
        , "Team"
        , "Opponent Name"
        , "Outcome"
    ]
    raw_schedule_cols_str = '", "'.join(raw_schedule_cols_list)

    joined_table_sql_query = f"""
        SELECT "{raw_schedule_cols_str}"
        FROM {load_from_schema}.{joined_input_name}
        ;
    """

    full_schedule = db_utils.sql_read_as_df(joined_table_sql_query)

    full_schedule['Outcome'] = full_schedule['Outcome'].map({'W':1, 'L':0})
    full_schedule['Location'] = full_schedule['Location'].map(
        {
            'Home': 1.0,
            'Semi-Home': 0.5,
            'Neutral': 0.0,
            'Semi-Away': -0.5,
            'Away': -1.0
        }
    )
    full_schedule.dropna(subset=["Outcome", "Location"], inplace=True)

    full_schedule["Date"] = pd.to_datetime(full_schedule["Date"]).dt.strftime('%Y%m%d')

    make_game_id = full_schedule.copy()
    make_game_id = pd.concat([
        make_game_id,
        pd.DataFrame(
            np.sort(make_game_id[["Team", "Opponent Name"]].values, axis=1)
            , columns=["Team A", "Team B"])
    ], axis=1)
    count_game_ids = make_game_id.groupby(["Date", "Team A", "Team B"], as_index=False).size()
    count_game_ids = count_game_ids[count_game_ids['size'] == 2]
    count_game_ids["Game ID"] = count_game_ids              \
                                    .reset_index(drop=True) \
                                    .index                  \
                                    .astype(str)            \
                                    .str.zfill(6)
    full_schedule = pd.merge(left=make_game_id
                                , right=count_game_ids
                                , how="inner"
                                , on=["Date", "Team A", "Team B"]
                                , validate="many_to_one"
    )
    full_schedule["Date"] = pd.to_datetime(full_schedule["Date"], format="%Y%m%d")
    full_schedule.sort_values(by=["Game ID"], ignore_index=True, inplace=True)
    full_schedule.reset_index(drop=True)
    full_schedule = full_schedule[["Game ID", "Season", "Team", "Opponent Name", "Location", "Outcome"]]

    full_schedule.rename(
        columns={"Game ID": "game_id"
                    , "Season": "season"
                    , "Team": "team_a"
                    , "Opponent Name": "team_b"
                    , "Location": "team_a_location"
                    , "Outcome": "team_a_outcome"
        }
        , inplace=True
        , errors="raise"
    )
    
    dtypes = {
        'game_id': Text()
        , 'season': Text()
        , 'team_a': Text()
        , 'team_b': Text()
        , 'team_a_location': Float()
        , 'team_a_outcome': Integer()
    }

    db_utils.sql_create_table(
                            df=full_schedule
                            , sql_table_name=clean_output_name
                            , save_to_schema=save_to_schema
                            , if_exists=if_exists
                            , dtype=dtypes
                            )

    # TODO: filter to only teams in Teams table
    # TODO: consider scheduling biases
    # TODO: rename column names to remove spaces and eliminate multiple renamings
    # TODO: build in read sql as datatypes (which will reduce reliance on to_datetime here)

    return None

create_clean_joined_schedule()
