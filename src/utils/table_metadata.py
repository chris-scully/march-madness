from kenpompy import utils as kenpompy_utils, \
                    summary as kenpompy_summary, \
                    team as kenpompy_team, \
                    misc as kenpompy_misc
"""
We renamed the above imports to avoid clashing with other 
usages of the variable "team" throughout the project.
"""

table_metadata = {
    "eff_stats": {
        "func": kenpompy_summary.get_efficiency
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "four_factors": {
        "func": kenpompy_summary.get_fourfactors
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "team_stats": {
        "func": kenpompy_summary.get_teamstats
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "points_dist": {
        "func": kenpompy_summary.get_pointdist
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "height": {
        "func": kenpompy_summary.get_height
        , "changes_yearly": True
        , "first_season": 2007
        , "exclude_from_load_all": False
    }, "player_stats": {
        "func": kenpompy_summary.get_playerstats
        , "changes_yearly": True
        , "first_season": 2007 # scraper is broken for this <2007
        , "exclude_from_load_all": False
    }, "kpoy": {
        "func": kenpompy_summary.get_kpoy
        , "changes_yearly": True
        , "first_season": 2011
        , "exclude_from_load_all": True
    }, "teams": {
        "func": kenpompy_team.get_valid_teams
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "schedule": {
        "func": kenpompy_team.get_schedule
        , "changes_yearly": True
        , "first_season": 2011
        , "exclude_from_load_all": True
    }, "ratings": {
        "func": kenpompy_misc.get_pomeroy_ratings
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "trends": {
        "func": kenpompy_misc.get_trends
        , "changes_yearly": False
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "refs": {
        "func": kenpompy_misc.get_refs
        , "changes_yearly": True
        , "first_season": 2016
        , "exclude_from_load_all": False
    }, "home_court_adv": {
        "func": kenpompy_misc.get_hca
        , "changes_yearly": False
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "arenas": {
        "func": kenpompy_misc.get_arenas
        , "changes_yearly": True
        , "first_season": 2010
        , "exclude_from_load_all": False
    }, "game_param": {
        "func": kenpompy_misc.get_gameattribs
        , "changes_yearly": True
        , "first_season": 2010
        , "exclude_from_load_all": False
    }, "program_ratings": {
        "func": kenpompy_misc.get_program_ratings
        , "changes_yearly": False
        , "first_season": 2002
        , "exclude_from_load_all": False
    }
}
