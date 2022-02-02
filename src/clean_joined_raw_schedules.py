from conf.kp_conf import kp_conf
from conf.db_conf import db_conf
from utils.db_utils import DB_Utils
from kenpompy import utils
import pandas as pd

browser = utils.login(kp_conf["email"], kp_conf["password"])

def create_master_datasets(joined_input_name=db_conf["raw_schedule_combined_tablename"],
                            load_from_schema=db_conf["staging_schema"],
                            browser=browser, 
                            save_to_schema=db_conf["clean_kenpom_data_schema"],
                            if_exists="replace",
                            random_seed = 42
    ):

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

    joined_schedules = joined_schedules[joined_schedules['Outcome'].isin(['W', 'L'])]
    joined_schedules = joined_schedules[joined_schedules['Location'].isin(['Home','Semi-Home','Neutral','Semi-Away','Away'])]

    joined_schedules['Outcome'].replace({'W':1, 'L':0}, inplace=True)
    joined_schedules['Location'].replace(
        {
            'Home': 1.0,
            'Semi-Home': 0.5,
            'Neutral': 0.0,
            'Semi-Away': -0.5,
            'Away': -1.0
        },
        inplace=True
    )

    joined_schedules_dup = joined_schedules.copy()
    joined_schedules_dup.rename(columns={"Team": "Opponent Name", "Opponent Name": "Team"}, inplace=True)
    joined_schedules_dup['Location'] = -1.0*joined_schedules_dup['Location']
    joined_schedules_dup['Outcome'] = 1-joined_schedules_dup['Outcome']

    full_schedule = pd.concat([joined_schedules, joined_schedules_dup], ignore_index=True)
    
    # TODO: add relevant features for model
    # TODO: conference adjustments
    print(full_schedule)

    return None

create_master_datasets()
