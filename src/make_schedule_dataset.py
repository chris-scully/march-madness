from utils.db_utils import DB_Utils

db_utils = DB_Utils()

sql_query = f''
df = db_utils.sql_read_as_df(sql_query)

# TODO: Write function that combines all raw KenPom schedules into one master table.