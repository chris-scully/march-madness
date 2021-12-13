from utils.db_utils import DB_Utils
import pandas.io.sql as psql

"""
This is a simple script to test whether or not `connect_to_database.py` 
and `config.py` are working properly.
"""

db_utils = DB_Utils()

create_table = """
    CREATE TABLE test (
        personId int,
        lastName varchar(255),
        firstName varchar(255)
    )
    ;
"""

insert_data = """
    INSERT INTO test (personId, lastName, firstName)
    VALUES (1, 'Luke', 'Wileczek')
    ;
"""

db_utils.sql_execute(create_table)
db_utils.sql_execute(insert_data)

df = db_utils.sql_read_as_df("SELECT * FROM test;")
row_count = len(df)

drop_table = """
    DROP TABLE IF EXISTS test;
    ;
"""

db_utils.sql_execute(drop_table)

if row_count == 1:
    print("Successfully tested connection.")
else:
    print("CONNECTION ERROR")
