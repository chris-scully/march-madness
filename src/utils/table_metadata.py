from kenpompy import utils, summary, team, misc

tables_metadata = {
    "eff_stats": {
        "func": summary.get_efficiency
        , "first_season": "2002"
    }, "four_factors": {
        "func": summary.get_fourfactors
        , "first_season": "2002"
    }, "team_stats": {
        "func": summary.get_teamstats
        , "first_season": "2002"
    }, "points_dist": {
        "func": summary.get_pointdist
        , "first_season": "2002"
    }, "height": {
        "func": summary.get_height
        , "first_season": "2007"
    }, "player_stats": {
        "func": summary.get_playerstats
        , "first_season": "2004"
    }, "kpoy": {
        "func": summary.get_kpoy
        , "first_season": "2011"
    }, "teams": {
        "func": team.get_valid_teams
        , "first_season": "2002"
    }, "schedule": {
        "func": team.get_schedule
        , "first_season": "2002"
    }, "ratings": {
        "func": misc.get_pomeroy_ratings
        , "first_season": "2002"
    }, "trends": {
        "func": misc.get_trends
        , "first_season": "2002"
    }, "refs": {
        "func": misc.get_refs
        , "first_season": "2016"
    }, "home_court_adv": {
        "func": misc.get_hca
        , "first_season": "2002"
    }, "arenas": {
        "func": misc.get_arenas
        , "first_season": "2010"
    }, "game_attr": {
        "func": misc.get_gameattribs
        , "first_season": "2010"
    }, "program_ratings": {
        "func": misc.get_program_ratings
        , "first_season": "2002"
    }
}
