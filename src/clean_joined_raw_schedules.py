from conf.kp_conf import kp_conf
from conf.db_conf import db_conf
from utils.db_utils import DB_Utils
from kenpompy import utils
import pandas as pd
from sqlalchemy import Integer, Float, Text

browser = utils.login(kp_conf["email"], kp_conf["password"])

def create_clean_joined_schedule(joined_input_name=db_conf["raw_schedule_combined_tablename"],
                            load_from_schema=db_conf["staging_schema"],
                            browser=browser, 
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

    joined_schedules = db_utils.sql_read_as_df(joined_table_sql_query)

    joined_schedules['Outcome'].map({'W':1, 'L':0}, inplace=True)
    joined_schedules['Location'].map(
        {
            'Home': 1.0,
            'Semi-Home': 0.5,
            'Neutral': 0.0,
            'Semi-Away': -0.5,
            'Away': -1.0
        },
        inplace=True
    )
    joined_schedules.dropna(subset=["Outcome", "Location"], inplace=True)

    joined_schedules_dup = joined_schedules.copy()
    joined_schedules_dup.rename(columns={"Team": "Opponent Name", "Opponent Name": "Team"}, inplace=True)
    joined_schedules_dup['Location'] = -1.0*joined_schedules_dup['Location']
    joined_schedules_dup['Outcome'] = 1-joined_schedules_dup['Outcome']

    full_schedule = pd.concat([joined_schedules, joined_schedules_dup], ignore_index=True)

    full_schedule.rename(
        columns={"Season": "Season"
                    , "Location": "Team A Location"
                    , "Team": "Team A"
                    , "Opponent Name": "Team B"
                    , "Outcome": "Team A Outcome"
        }
        , inplace=True
        , errors="raise"
    )
    full_schedule = full_schedule.reindex(
        columns=[
            "Season"
            , "Team A"
            , "Team B"
            , "Team A Location"
            , "Team A Outcome"
        ]
    )
    
    dtypes = {
        'Season': Text()
        , 'Team A': Text()
        , 'Team B': Text()
        , 'Team A Location': Float()
        , 'Team A Outcome': Integer()
    }
    db_utils.sql_create_table(
                            df=full_schedule
                            , sql_table_name=clean_output_name
                            , save_to_schema=save_to_schema
                            , if_exists=if_exists
                            , dtype=dtypes
                            )

    return None
