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
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": True
    }, "four_factors": {
        "func": kenpompy_summary.get_fourfactors
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": True
    }, "team_stats": {
        "func": kenpompy_summary.get_teamstats
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": True
    }, "points_dist": {
        "func": kenpompy_summary.get_pointdist
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": True
    }, "height": {
        "func": kenpompy_summary.get_height
        , "changes_yearly": True
        , "first_season": 2007
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": True
    }, "player_stats": {
        "func": kenpompy_summary.get_playerstats
        , "changes_yearly": True
        , "first_season": 2007
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }, "kpoy": {
        "func": kenpompy_summary.get_kpoy
        , "changes_yearly": True
        , "first_season": 2011
        , "include_in_load_all": False
        , "include_as_feature_in_master_dataset": False
    }, "teams": {
        "func": kenpompy_team.get_valid_teams
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }, "schedule": {
        "func": kenpompy_team.get_schedule
        , "changes_yearly": True
        , "first_season": 2011
        , "include_in_load_all": False
        , "include_as_feature_in_master_dataset": False
    }, "ratings": {
        "func": kenpompy_misc.get_pomeroy_ratings
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": True
    }, "trends": {
        "func": kenpompy_misc.get_trends
        , "changes_yearly": False
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }, "refs": {
        "func": kenpompy_misc.get_refs
        , "changes_yearly": True
        , "first_season": 2016
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }, "home_court_adv": {
        "func": kenpompy_misc.get_hca
        , "changes_yearly": False
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }, "arenas": {
        "func": kenpompy_misc.get_arenas
        , "changes_yearly": True
        , "first_season": 2010
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }, "game_param": {
        "func": kenpompy_misc.get_gameattribs
        , "changes_yearly": True
        , "first_season": 2010
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }, "program_ratings": {
        "func": kenpompy_misc.get_program_ratings
        , "changes_yearly": False
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_as_feature_in_master_dataset": False
    }
}
