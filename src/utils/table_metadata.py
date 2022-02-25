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
        , "include_fields_in_master_dataset": True
        , "fields": {
            "Team": {
                "to_load": True
                , "rename_to": "team"
            }, 
            "Conference": {
                "to_load": False
                , "rename_to": "conference"
            }, 
            "Tempo-Adj": {
                "to_load": True
                , "rename_to": "tempo_adj"
            }, 
            "Tempo-Adj.Rank": {
                "to_load": False
                , "rename_to": "tempo_adj_rank"
            }, 
            "Tempo-Raw": {
                "to_load": False
                , "rename_to": "tempo_raw"
            }, 
            "Tempo-Raw.Rank": {
                "to_load": False
                , "rename_to": "tempo_raw_rank"
            }, 
            "Avg. Poss Length-Offense": {
                "to_load": True
                , "rename_to": "avg_poss_length_off"
            }, 
            "Avg. Poss Length-Offense.Rank": {
                "to_load": False
                , "rename_to": "avg_poss_length_off_rank"
            }, 
            "Avg. Poss Length-Defense": {
                "to_load": True
                , "rename_to": "avg_poss_length_deff"
            }, 
            "Avg. Poss Length-Defense.Rank": {
                "to_load": False
                , "rename_to": "avg_poss_length_def_rank"
            }, 
            "Off. Efficiency-Adj": {
                "to_load": True
                , "rename_to": "off_eff_adj"
            }, 
            "Off. Efficiency-Adj.Rank": {
                "to_load": False
                , "rename_to": "off_eff_adj_rank"
            }, 
            "Off. Efficiency-Raw": {
                "to_load": False
                , "rename_to": "off_eff_raw"
            }, 
            "Off. Efficiency-Raw.Rank": {
                "to_load": False
                , "rename_to": "off_eff_adj_rank"
            }, 
            "Def. Efficiency-Adj": {
                "to_load": True
                , "rename_to": "def_eff_adj"
            }, 
            "Def. Efficiency-Adj.Rank": {
                "to_load": False
                , "rename_to": "def_eff_adj_rank"
            }, 
            "Def. Efficiency-Raw": {
                "to_load": False
                , "rename_to": "def_eff_raw"
            }, 
            "Def. Efficiency-Raw.Rank": {
                "to_load": False
                , "rename_to": "def_eff_raw_rank"
            }
        }
    }, "four_factors": {
        "func": kenpompy_summary.get_fourfactors
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": True
        , "fields": {
            "Team": {
                "to_load": True
                , "rename_to": "team"
            },
            "Conference": {
                "to_load": False
                , "rename_to": "conference"
            },
            "AdjTempo": {
                "to_load": False
                , "rename_to": "tempo_adj"
            },
            "AdjTempo.Rank": {
                "to_load": False
                , "rename_to": "tempo_adj_rank"
            },
            "AdjOE": {
                "to_load": False
                , "rename_to": "off_eff_adj"
            },
            "AdjOE.Rank": {
                "to_load": False
                , "rename_to": "off_eff_adj_rank"
            },
            "Off-eFG%": {
                "to_load": True
                , "rename_to": "off_eff_fg_perc"
            },
            "Off-eFG%.Rank": {
                "to_load": False
                , "rename_to": "off_eff_fg_perc_rank"
            },
            "Off-TO%": {
                "to_load": True
                , "rename_to": "off_to_perc"
            },
            "Off-TO%.Rank": {
                "to_load": False
                , "rename_to": "off_to_perc"
            },
            "Off-OR%": {
                "to_load": True
                , "rename_to": "off_off_reb_perc"
            },
            "Off-OR%.Rank": {
                "to_load": False
                , "rename_to": "off_off_reb_perc_rank"
            },
            "Off-FTRate": {
                "to_load": True
                , "rename_to": "off_ft_perc"
            },
            "Off-FTRate.Rank": {
                "to_load": False
                , "rename_to": "off_ft_perc_rank"
            },
            "AdjDE": {
                "to_load": False
                , "rename_to": "def_eff_adj"
            },
            "AdjDE.Rank": {
                "to_load": False
                , "rename_to": "def_eff_adj_rank"
            },
            "Def-eFG%": {
                "to_load": True
                , "rename_to": "def_eff_fg_perc"
            },
            "Def-eFG%.Rank": {
                "to_load": False
                , "rename_to": "def_eff_fg_perc_rank"
            },
            "Def-TO%": {
                "to_load": True
                , "rename_to": "def_to_perc"
            },
            "Def-TO%.Rank": {
                "to_load": False
                , "rename_to": "def_to_perc"
            },
            "Def-OR%": {
                "to_load": True
                , "rename_to": "def_off_reb_perc"
            },
            "Def-OR%.Rank": {
                "to_load": False
                , "rename_to": "def_off_reb_perc_rank"
            },
            "Def-FTRate": {
                "to_load": True
                , "rename_to": "def_ft_perc"
            },
            "Def-FTRate.Rank": {
                "to_load": False
                , "rename_to": "def_ft_perc_rank"
            }
        }
    }, "team_stats": {
        "func": kenpompy_summary.get_teamstats
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": True
        , "fields": {
            "Team": {
                "to_load": True
                , "rename_to": "team"
            },
            "Conference": {
                "to_load": True
                , "rename_to": "conference"
            },
            "3P%": {
                "to_load": True
                , "rename_to": "three_pt_perc"
            },
            "3P%.Rank": {
                "to_load": False
                , "rename_to": "three_pt_perc_rank"
            },
            "2P%": {
                "to_load": True
                , "rename_to": "two_pt_perc"
            },
            "2P%.Rank": {
                "to_load": False
                , "rename_to": "two_pt_perc_rank"
            },
            "FT%": {
                "to_load": False
                , "rename_to": "ft_perc"
            },
            "FT%.Rank": {
                "to_load": False
                , "rename_to": "ft_perc_rank"
            },
            "Blk%": {
                "to_load": True
                , "rename_to": "blk_perc"
            },
            "Blk%.Rank": {
                "to_load": False
                , "rename_to": "blk_perc_rank"
            },
            "Stl%": {
                "to_load": True
                , "rename_to": "stl_perc"
            },
            "Stl%.Rank": {
                "to_load": False
                , "rename_to": "stl_perc_rank"
            },
            "A%": {
                "to_load": True
                , "rename_to": "ass_perc"
            },
            "A%.Rank": {
                "to_load": False
                , "rename_to": "ass_perc_rank"
            },
            "3PA%": {
                "to_load": True
                , "rename_to": "three_pt_att_perc"
            }
        }
    }, "points_dist": {
        "func": kenpompy_summary.get_pointdist
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": True
        , "fields": {
            "Team": {
                "to_load": True
                , "rename_to": "team"
            },
            "Conference": {
                "to_load": False
                , "rename_to": "conference"
            },
            "Off-FT": {
                "to_load": True
                , "rename_to": "off_dist_ft"
            },
            "Off-FT.Rank": {
                "to_load": False
                , "rename_to": "off_dist_ft_rank"
            },
            "Off-2P": {
                "to_load": True
                , "rename_to": "off_dist_two"
            },
            "Off-2P.Rank": {
                "to_load": False
                , "rename_to": "off_dist_two_rank"
            },
            "Off-3P": {
                "to_load": True
                , "rename_to": "off_dist_three"
            },
            "Off-3P.Rank": {
                "to_load": False
                , "rename_to": "off_dist_three_rank"
            },
            "Def-FT": {
                "to_load": True
                , "rename_to": "def_dist_ft"
            },
            "Def-FT.Rank": {
                "to_load": False
                , "rename_to": "def_dist_ft_rank"
            },
            "Def-2P": {
                "to_load": True
                , "rename_to": "def_dist_two"
            },
            "Def-2P.Rank": {
                "to_load": False
                , "rename_to": "def_dist_two_rank"
            },
            "Def-3P": {
                "to_load": True
                , "rename_to": "def_dist_three"
            },
            "Def-3P.Rank": {
                "to_load": False
                , "rename_to": "def_dist_three_rank"
            }
        }
    }, "height": {
        "func": kenpompy_summary.get_height
        , "changes_yearly": True
        , "first_season": 2007
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": True
        , "fields": {
            "Team": {
                "to_load": True
                , "rename_to": "team"
            },
            "Conference": {
                "to_load": False
                , "rename_to": "conference"
            },
            "AvgHgt": {
                "to_load": True
                , "rename_to": "avg_hght"
            },
            "AvgHgt.Rank": {
                "to_load": False
                , "rename_to": "avg_hght_rank"
            },
            "EffHgt": {
                "to_load": True
                , "rename_to": "avg_eff_hght"
            },
            "EffHgt.Rank": {
                "to_load": False
                , "rename_to": "avg_eff_hght_rank"
            },
            "C-Hgt": {
                "to_load": True
                , "rename_to": "avg_c_hght"
            },
            "C-Hgt.Rank": {
                "to_load": False
                , "rename_to": "avg_c_hght_rank"
            },
            "PF-Hgt": {
                "to_load": True
                , "rename_to": "avg_pf_hght"
            },
            "PF-Hgt.Rank": {
                "to_load": False
                , "rename_to": "avg_pf_hght_rank"
            },
            "SF-Hgt": {
                "to_load": True
                , "rename_to": "avg_sf_hght"
            },
            "SF-Hgt.Rank": {
                "to_load": False
                , "rename_to": "avg_sf_hght_rank"
            },
            "SG-Hgt": {
                "to_load": True
                , "rename_to": "avg_sg_hght"
            },
            "SG-Hgt.Rank": {
                "to_load": False
                , "rename_to": "avg_sg_hght_rank"
            },
            "PG-Hgt": {
                "to_load": True
                , "rename_to": "avg_pg_hght"
            },
            "PG-Hgt.Rank": {
                "to_load": False
                , "rename_to": "avg_pg_hght_rank"
            },
            "Experience": {
                "to_load": True
                , "rename_to": "experience"
            },
            "Experience.Rank": {
                "to_load": False
                , "rename_to": "experience_rank"
            },
            "Bench": {
                "to_load": True
                , "rename_to": "bench_min"
            },
            "Bench.Rank": {
                "to_load": False
                , "rename_to": "bench_min_rank"
            },
            "Continuity": {
                "to_load": True
                , "rename_to": "continuity"
            },
            "Continuity.Rank": {
                "to_load": False
                , "rename_to": "continuity_rank"
            }
        }
    }, "player_stats": {
        "func": kenpompy_summary.get_playerstats
        , "changes_yearly": True
        , "first_season": 2007
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": False
        , "fields": {
            "Rank": {
                "to_load": False
                , "rename_to": "rank"
            },
            "Player": {
                "to_load": False
                , "rename_to": "player"
            },
            "Team": {
                "to_load": False
                , "rename_to": "team"
            },
            "EFG": {
                "to_load": False
                , "rename_to": "off_eff_fg_perc"
            },
            "Ht": {
                "to_load": False
                , "rename_to": "height"
            },
            "Wt": {
                "to_load": False
                , "rename_to": "weight"
            },
            "Yr": {
                "to_load": False
                , "rename_to": "year"
            }
        }
    }, "kpoy": {
        "func": kenpompy_summary.get_kpoy
        , "changes_yearly": True
        , "first_season": 2011
        , "include_in_load_all": False
        , "include_fields_in_master_dataset": False
        , "fields": {}
    }, "teams": {
        "func": kenpompy_team.get_valid_teams
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": False
        , "fields": {
            "Teams": {
                "to_load": True
                , "rename_to": "team"
            }
        }
    }, "schedule": {
        "func": kenpompy_team.get_schedule
        , "changes_yearly": True
        , "first_season": 2011
        , "include_in_load_all": False
        , "include_fields_in_master_dataset": False
        , "fields": {} # TODO: implement renaming here
    }, "ratings": {
        "func": kenpompy_misc.get_pomeroy_ratings
        , "changes_yearly": True
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": True
        , "fields": {
            "Rk": {
                "to_load": False
                , "rename_to": "rank"
            },
            "Team": {
                "to_load": True
                , "rename_to": "team"
            },
            "Conf": {
                "to_load": False
                , "rename_to": "conference"
            },
            "W-L": {
                "to_load": False
                , "rename_to": "record"
            },
            "AdjEM": {
                "to_load": False
                , "rename_to": "eff_margin"
            },
            "AdjO": {
                "to_load": False
                , "rename_to": "off_eff_adj"
            },
            "AdjD": {
                "to_load": False
                , "rename_to": "def_eff_adj"
            },
            "AdjT": {
                "to_load": False
                , "rename_to": "off_adj_temp"
            },
            "Luck": {
                "to_load": False
                , "rename_to": "luck"
            },
            "OppO": {
                "to_load": True
                , "rename_to": "avg_opp_off_eff_adj"
            },
            "OppD": {
                "to_load": True
                , "rename_to": "avg_opp_odef_eff_adj"
            },
            "Seed": {
                "to_load": False
                , "rename_to": "seed"
            }
        }
    }, "trends": {
        "func": kenpompy_misc.get_trends
        , "changes_yearly": False
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": False
        , "fields": {}
        }
    }, "refs": {
        "func": kenpompy_misc.get_refs
        , "changes_yearly": True
        , "first_season": 2016
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": False
        , "fields": {}
        }
    }, "home_court_adv": {
        "func": kenpompy_misc.get_hca
        , "changes_yearly": False
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": False
        , "fields": {}
        }
    }, "arenas": {
        "func": kenpompy_misc.get_arenas
        , "changes_yearly": True
        , "first_season": 2010
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": False
        , "fields": {}
        }
    }, "program_ratings": {
        "func": kenpompy_misc.get_program_ratings
        , "changes_yearly": False
        , "first_season": 2002
        , "include_in_load_all": True
        , "include_fields_in_master_dataset": False
        , "fields": {}
        }
    }
}
