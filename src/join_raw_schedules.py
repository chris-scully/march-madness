from conf.kp_conf import kp_conf
from conf.db_conf import db_conf
from utils.db_utils import DB_Utils
from kenpompy import utils
import pandas as pd
import time
from sqlalchemy import Integer, Date, Text

browser = utils.login(kp_conf["email"], kp_conf["password"])

def join_raw_schedules(joined_output_name=db_conf["raw_schedule_combined_tablename"], 
                        browser=browser, 
                        load_from_schema=db_conf["raw_kenpom_schedule_schema"],
                        save_to_schema=db_conf["staging_schema"],
                        if_exists="replace"
):
    """
    Function to load all saved raw KenPom tables from the database,
    join them into one master multi-year schedule, and push the
    master back to the database.

    Args:
        joined_output_name (str): 
            Name of output table in database.
            Defaults to db_conf["raw_schedule_combined_tablename"].
        browser (optional):
            Should not need to edit this. Uses config kenpom credentials.
            Defaults to browser.
        save_to_schema (str, optional): [description]. 
            The schema to which the output table is saved
            Defaults to db_conf["staging_schema"].
        if_exists (str, optional): 
            follows if_exists from https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
            Defaults to "replace".
    """    

    
    db_utils = DB_Utils()

    all_tables_sql_query = f"""
        SELECT tablename 
        FROM pg_tables
        WHERE schemaname = '{load_from_schema}'
        ;
    """
    raw_schedule_list = db_utils.sql_read_as_df(all_tables_sql_query)['tablename'].tolist()

    raw_schedule_cols_list = [
        "Date"
        , "Location"
        , "Team"
        , "Team Points"
        , "Opponent Name"
        , "Opponent Points"
        , "Outcome"
    ]
    raw_schedule_cols_str = '", "'.join(raw_schedule_cols_list)
    joined_schedules = pd.DataFrame(columns=["Season"]+raw_schedule_cols_list)
    sleep_time = 1
    for raw_schedule in raw_schedule_list:
        raw_schedule_sql_query = f"""
            SELECT "{raw_schedule_cols_str}"
            FROM {load_from_schema}."{raw_schedule}"
            ;
            """
        raw_schedule_df = db_utils.sql_read_as_df(raw_schedule_sql_query)
        raw_schedule_df['Season'] = raw_schedule[0:4]
        joined_schedules = pd.concat([joined_schedules, raw_schedule_df])
        time.sleep(sleep_time)

    dtypes = {
            'Date': Date()
            , 'Location': Text()
            , 'Team': Text()
            , 'Team Points': Integer()
            , 'Opponent Name': Text()
            , 'Opponent Points': Integer()
            , 'Outcome': Text()
            }
    db_utils.sql_create_table(
                            df=joined_schedules
                            , sql_table_name=joined_output_name
                            , save_to_schema=save_to_schema
                            , if_exists=if_exists
                            , dtype=dtypes
                            )
