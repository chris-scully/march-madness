from functools import reduce

# TODO: Move etl functions into this file
def join_tables(list_of_dfs, keys="Team", type="left"):
    df_final = reduce(lambda left,right: pd.merge(left,right,on='name'), dfs)
    return df_final
