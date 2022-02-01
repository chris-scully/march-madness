# march-madness

## KenPom Data Dictionary

### ratings
**AdjEM**: Adjusted Efficency Margin - Simple subtraction between a team’s offensive and defensive efficiency

**AdjO**: Adjusted offensive efficiency – An estimate of the offensive efficiency (points scored per 100 possessions) a team would have against the average D-I defense.

**AdjD**: Adjusted defensive efficiency – An estimate of the defensive efficiency (points allowed per 100 possessions) a team would have against the average D-I offense.

**AdjT**: An estimate of the tempo (possessions per 40 minutes) a team would have against the team that wants to play at an average D-I tempo.

**Luck**: A measure of the deviation between a team’s actual winning percentage and what one would expect from its game-by-game efficiencies. It’s a Dean Oliver invention. Essentially, a team involved in a lot of close games should not win (or lose) all of them. Those that do will be viewed as lucky (or unlucky).

**OppO**: Average AdjO of opposing offenses

**OppD**: Average AdjD of opposing offenses

### eff_stats
**Tempo-Adj** [Duplicate]

**Tempo-Raw**: Possessions per 40 minutes

**Avg. Poss Length-Offense**: Average length of a team's possessions in seconds

**Avg. Poss Length-Defense**: Average length of opposing teams possessions in seconds

**Off. Efficiency-Adj.Rank** [Duplicate]

**Off. Efficiency-Raw.Rank**: Points scored per 100 possessions

**Def. Efficiency-Adj.Rank** [Duplicate]

**Def. Efficiency-Raw.Rank**: Points allowed per 100 possessions

### four_factors
**AdjTempo** [Duplicate]

**AdjOE** [Duplicate]

**Off-eFG%**: (FGM + 0.5*3PM)/FGA for the offense

**Off-TO%**: TO/Possessions for the offense

**Off-OR%**: OR / (OR + DR) - Percentage of possible offensive rebounds a team gets

**Off-FTRate**: FTA/FGA for the offense

**AdjDE** [Duplicate]

**Def-eFG%**: (FGM + 0.5*3PM)/FGA for the defense

**Def-TO%**: TO/Possessions for the defense

**Def-OR%**: OR / (OR + DR) - Percentage of possible offensive rebounds the opposing team gets

**Def-FTRate**: FTA/FGA for the defense

### height
**AvgHgt**: Overall average height is computed by taking the average listed height of every player on the team, weighted by minutes played. Players that have played less than 10% of their team’s minutes are not included.

**EffHgt**: Effective height is the average of the center and power forward position. 

**C-Hgt**: To calculate the positional height data, the minutes played for each team are ordered by height. Thus the 20% of minutes played by the tallest players are assumed to be center minutes, the next 20% are assumed to be power forward minutes, etc.

**PF-Hgt**: To calculate the positional height data, the minutes played for each team are ordered by height. Thus the 20% of minutes played by the tallest players are assumed to be center minutes, the next 20% are assumed to be power forward minutes, etc.

**SF-Hgt**: To calculate the positional height data, the minutes played for each team are ordered by height. Thus the 20% of minutes played by the tallest players are assumed to be center minutes, the next 20% are assumed to be power forward minutes, etc.

**SG-Hgt**: To calculate the positional height data, the minutes played for each team are ordered by height. Thus the 20% of minutes played by the tallest players are assumed to be center minutes, the next 20% are assumed to be power forward minutes, etc.

**PG-Hgt**: To calculate the positional height data, the minutes played for each team are ordered by height. Thus the 20% of minutes played by the tallest players are assumed to be center minutes, the next 20% are assumed to be power forward minutes, etc.

**Experience**: The experience value is in terms of years of college experience where a player’s eligibility class is assumed to determine this. For the purposes of the calculation, a freshman has zero years of experience, a sophomore has one year of experience, etc. The experience calculation weights the experience of each player on the roster based on minutes played. Players that have played less than 10% of their team’s minutes are not included.

**Bench**: Bench minutes are computed by assuming that the starters are the five players that have played the most minutes on the season. The minutes of remaining players are all assumed to be bench minutes. Players that have played less than 10% of their team’s minutes are not included.

**Continuity**: What percentage of a team’s minutes are played by the same player from last season to this season

### team_stats_off
**3P%**: 3-point percentage

**2P%**: 2-point percentage

**FT%**: free-throw percentage

**Blk%**: (blocked shots) / (opponents’ field goal attempts)

**Stl%**: Steals / Defensive possessions

**A%**: Assists divided by teammates’ made field goals, scaled for playing time

**3PA%**: Percentage of field goals from three-point range

**AdjOE** [Duplicate]

### team_stats_def

### points_dist
**Off-FT**: Percentage of offensive points coming from free throws

**Off-2P**: Percentage of offensive points coming from 2-pointers

**Off-3P**: Percentage of offensive points coming from 3-pointers

**Def-FT**: Percentage of defensive points coming from free throws

**Def-2P**: Percentage of defensive points coming from 2-pointers

**Def-3P**: Percentage of defensive points coming from 3-pointers
