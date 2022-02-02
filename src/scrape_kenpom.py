from conf.kp_conf import kp_conf
from conf.db_conf import db_conf
from kenpompy import utils, summary, team, misc
from utils.table_metadata import table_metadata
from utils.db_utils import DB_Utils
import time
import itertools
from sqlalchemy import Integer, Date, Text
import pandas as pd
import numpy as np

current_season = 2022
sleep_time = 5

# Log-in to kenpom.com
browser = utils.login(kp_conf["email"], kp_conf["password"])

def scrape_kenpom_data(tables="all", 
                        seasons="all", 
                        if_exists="replace", 
                        browser=browser, 
                        save_to_schema=db_conf["raw_kenpom_data_schema"]
):
    """
    Function to scrape (or re-scrape) data tables from kenpom.com, cleanse, and save to our database.

    Args:
        tables (str or list[string], optional): Defaults to "all"
            "all" re-loads all tables
            can pass in a single string if only wish to re-load one table
            to re-load multiple tables, can use a list of the table names as strings; table names are:
                eff_stats, four_factors, team_stats, points_dist, height, player_stats, kpoy, teams, 
                schedule, ratings, trends, refs, home_court_adv, arenas, game_attr, program_ratings
        seasons (str or list[str], optional): Defaults to "all"
            "all" re-loads all seasons
            to reload a single season, can use an string for the year (i.e. for 2021-2022 season, use '2022')
            to reload multiple seasons, use a list of years as strings
        if_exists (str, optional): follows if_exists from https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
        browser: Should not need to edit this. Uses config kenpom credentials.
        save_to_schema (str, optional): the database schema to save data to

    Returns:
        None
    """
    all_kenpom_tables = list(table_metadata.keys())

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
    for table in tables_to_update:
        if not table_metadata[table]["exclude_from_load_all"]:
            changes_yearly = table_metadata[table]["changes_yearly"]
            if changes_yearly:
                for season in seasons_to_update:
                    first_season = table_metadata[table]["first_season"]
                    if int(season) >= first_season:
                        func = table_metadata[table]["func"]
                        time.sleep(sleep_time)
                        try:
                            if table != "team_stats":
                                data = func(browser=browser, season=season)
                                if table == "teams":
                                    df = pd.DataFrame(data, columns=["Teams"])
                                    df['Teams'] = df['Teams'].str.replace('*', '').str.strip()  
                                else:
                                    df = data
                                db_utils.sql_create_table(
                                    df=df,
                                    sql_table_name=season + "_" + table, 
                                    save_to_schema=save_to_schema, 
                                    if_exists=if_exists
                                )
                            else:
                                off_def = [("off", False), ("def", True)]
                                for suffix, def_bool in off_def:
                                    df = func(browser=browser, defense=def_bool, season=season)
                                    db_utils.sql_create_table(
                                        df=df,
                                        sql_table_name=season + "_" + table + "_" + suffix,
                                        save_to_schema=save_to_schema, 
                                        if_exists=if_exists
                                    )
                        except Exception as e:
                            print(f"ERROR (table: {table}, season: {season}): {str(e)}")
            else:
                time.sleep(sleep_time)
                try:
                    df = func(browser=browser)
                    db_utils.sql_create_table(
                        df=df, 
                        sql_table_name=table, 
                        save_to_schema=save_to_schema, 
                        if_exists=if_exists
                    )
                    # print(f"Successfully pushed table: table.")
                except Exception as e:
                    print(f"ERROR (table: {table}, season: {season}): {str(e)}")

    return None

def scrape_kenpom_schedules(if_exists="replace", 
                            browser=browser, 
                            teams_schema=db_conf["raw_kenpom_data_schema"],
                            save_to_schema=db_conf["raw_kenpom_schedule_schema"]
):
    """
    Function to scrape (or re-scrape) schedule tables from kenpom.com, cleanse, and save to our database.

    Args:
        if_exists (str, optional): follows if_exists from https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
        browser: Should not need to edit this. Uses config kenpom credentials.
        save_to_schema (str, optional): the database schema to save data to

    Returns:
        None
    """

    # Generate list of tuples (team, year) that have scheduling information per season
    db_utils = DB_Utils()
    all_seasons = list(map(str, range(table_metadata["schedule"]["first_season"], current_season+1)))
    all_teams_by_year = pd.DataFrame(columns=['Teams', 'Year'])
    for season in all_seasons:
        sql_query = f'SELECT "Teams" FROM {teams_schema}."{season}_teams"'
        all_teams_by_one_year = db_utils.sql_read_as_df(sql_query)
        all_teams_by_one_year['Year'] = season
        all_teams_by_year = pd.concat([all_teams_by_year, all_teams_by_one_year])
    team_seasons_tpl = list(zip(all_teams_by_year['Teams'], all_teams_by_year['Year']))
    team_seasons_df = all_teams_by_year[['Teams', 'Year']]
    
    # Load and clean team schedules from KenPom
    for team, season in team_seasons_tpl:
        # Load schedule
        func = table_metadata["schedule"]["func"]
        try:
            schedule = func(browser=browser, team=team, season=season)
        except Exception as e:
            print(f'ERROR: {season} {team} failed due to: {e}')
            continue

        # Filter out extra data picked up by scraper
        schedule['Team'] = team
        teams_list = team_seasons_df[team_seasons_df['Year'] == season]['Teams'].tolist()
        col_list = ['Date', 'Location', 'Team', 'Opponent Name', 'Result']
        schedule = schedule.loc[schedule['Opponent Name'].isin(teams_list), col_list]

        # Cleanse 'Date' column
        days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        prev_year_mths = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        schedule['Date'] = schedule['Date'].str.replace('|'.join(days_of_week), '').str.strip()
        schedule['Date'] = schedule['Date'].apply(
            lambda d: d + ' ' + str(int(season)-1) if d[0:3] in prev_year_mths else d + ' ' + season
            )
        schedule['Date'] = pd.to_datetime(schedule['Date'], format='%b %d %Y', errors='coerce').dt.date
        schedule = schedule.dropna(subset=['Date'])

        # Cleanse Result column
        schedule['Outcome'] = schedule['Result'].str.split(',').str[0].str.strip()
        schedule['Result'] = schedule['Result'].str.split(',').str[1].str.strip()
        schedule['Team Points'] = np.where(
            schedule['Outcome'] == 'W', 
            schedule['Result'].str.split('-').str[0].str.strip(), 
            schedule['Result'].str.split('-').str[1].str.strip()
            ).astype(int)
        schedule['Opponent Points'] = np.where(
            schedule['Outcome'] != 'W', 
            schedule['Result'].str.split('-').str[0].str.strip(), 
            schedule['Result'].str.split('-').str[1].str.strip()
            ).astype(int)
        schedule = schedule[['Date', 'Location', 'Team', 'Team Points', 'Opponent Name', 'Opponent Points', 'Outcome']]
        
        # Push schedule to database
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
                                df=schedule
                                , sql_table_name = season + "_" + team + "_Schedule" 
                                , save_to_schema=save_to_schema
                                , if_exists=if_exists
                                , dtype=dtypes
                            )
        time.sleep(sleep_time)

    return None
