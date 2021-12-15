from kenpompy import utils, summary, team, misc

tables_metadata = {
    "eff_stats": {
        "func": summary.get_efficiency
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "four_factors": {
        "func": summary.get_fourfactors
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "team_stats": {
        "func": summary.get_teamstats
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "points_dist": {
        "func": summary.get_pointdist
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "height": {
        "func": summary.get_height
        , "changes_yearly": True
        , "first_season": 2007
        , "exclude_from_load_all": False
    }, "player_stats": {
        "func": summary.get_playerstats
        , "changes_yearly": True
        , "first_season": 2007 # scraper is broken for this <2007
        , "exclude_from_load_all": False
    }, "kpoy": {
        "func": summary.get_kpoy
        , "changes_yearly": True
        , "first_season": 2011
        , "exclude_from_load_all": True
    }, "teams": {
        "func": team.get_valid_teams
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "schedule": {
        "func": team.get_schedule
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": True
    }, "ratings": {
        "func": misc.get_pomeroy_ratings
        , "changes_yearly": True
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "trends": {
        "func": misc.get_trends
        , "changes_yearly": False
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "refs": {
        "func": misc.get_refs
        , "changes_yearly": True
        , "first_season": 2016
        , "exclude_from_load_all": False
    }, "home_court_adv": {
        "func": misc.get_hca
        , "changes_yearly": False
        , "first_season": 2002
        , "exclude_from_load_all": False
    }, "arenas": {
        "func": misc.get_arenas
        , "changes_yearly": True
        , "first_season": 2010
        , "exclude_from_load_all": False
    }, "game_param": {
        "func": misc.get_gameattribs
        , "changes_yearly": True
        , "first_season": 2010
        , "exclude_from_load_all": False
    }, "program_ratings": {
        "func": misc.get_program_ratings
        , "changes_yearly": False
        , "first_season": 2002
        , "exclude_from_load_all": False
    }
}
