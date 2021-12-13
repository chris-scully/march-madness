from conf.kp_conf import kp_conf
from kenpompy import utils, summary, team, misc
from utils.table_metadata import tables_metadata
from utils.db_utils import DB_Utils
import time
import itertools
import pandas as pd

current_season = 2022

# Log-in to kenpom.com
browser = utils.login(kp_conf["email"], kp_conf["password"])

def load_kenpom_data(tables="all", seasons="all", if_exists="replace", browser=browser):
    """
    Function to load (or re-load) tables from kenpom.com

    Args:
        tables (str or list[string], optional): Defaults to "all"
            "all" re-loads all tables
            can pass in a single string is only wish to re-load one table
            to re-load multiple tables, can use a list of the table names as strings; table names are:
                eff_stats, four_factors, team_stats, points_dist, height, player_stats, kpoy, teams, 
                schedule, ratings, trends, refs, home_court_adv, arenas, game_attr, program_ratings
        seasons (str or integer or list[integer], optional): Defaults to "all"
            "all" re-loads all seasons
            to reload a single season, can use an string for the year (i.e. for 2021-2022 season, use '2022')
            to reload multiple seasons, use a list of years as strings
        browser: Should not need to edit this. Uses config kenpom credentials.

    Returns:
        None
    """
    all_kenpom_tables = list(tables_metadata.keys())

    all_seasons = list(map(str, range(2002, current_season+1)))

    # Build list of tables to update
    tables_to_update = []
    if tables == "all":
        tables_to_update = all_kenpom_tables
    elif isinstance(tables, str) and tables in all_kenpom_tables:
        tables_to_update = [tables]
    elif isinstance(tables, list) and all(tbls in all_kenpom_tables for tbls in tables):
        tables_to_update = tables

    # Build list of seasons to update
    seasons_to_update = []
    if seasons == "all":
        seasons_to_update = all_seasons
    elif isinstance(seasons, str) and seasons in all_seasons:
        seasons_to_update = [seasons]
    elif isinstance(seasons, list) and all(ssns in all_seasons for ssns in seasons):
        seasons_to_update = seasons

    # Scraping from KenPom.com and pushing to our PostreSQL DB
    db_utils = DB_Utils()
    sleep_time = 5
    for table in tables_to_update:
        if not tables_metadata[table]["exclude_from_load_all"]:
            func = tables_metadata[table]["func"]
            changes_yearly = tables_metadata[table]["changes_yearly"]
            if changes_yearly:
                first_season = tables_metadata[table]["first_season"]
                for season in seasons_to_update:
                    if int(season) >= first_season:
                        time.sleep(sleep_time)
                        try:
                            data = func(browser=browser, season=season)
                            df = data if table != "teams" else pd.DataFrame(data, columns=["Teams"])
                            sql_table_name = season + "_" + table
                            db_utils.sql_create_table(df=df, sql_table_name=sql_table_name, if_exists=if_exists)
                            # print(f"Successfully pushed table: sql_table_name.")
                        except Exception as e:
                            print(f"ERROR (table: {table}, season: {season}): {str(e)}")
            else:
                time.sleep(sleep_time)
                try:
                    df = func(browser=browser)
                    db_utils.sql_create_table(df=df, sql_table_name=table, if_exists=if_exists)
                    # print(f"Successfully pushed table: table.")
                except Exception as e:
                    print(f"ERROR (table: {table}, season: {season}): {str(e)}")

    return None

# TODO: following errors with this script:
# teams:'list' object has no attribute 'to_sql' (maybe fixed?)
# player_stats: Length mismatch: Expected axis has 4 elements, new values have 7 elements (only in 2004-2006)
# remove yearly tables from postgres for tables that shouldn't have a year
