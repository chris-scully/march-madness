from connect_to_database import connect_to_database
import pandas.io.sql as psql

"""
This is a simple script to test whether or not `connect_to_database.py` 
and `config.py` are working properly.
"""

conn = connect_to_database()
cursor = conn.cursor()

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


cursor.execute(create_table)
cursor.execute(insert_data)

df = psql.read_sql("SELECT * FROM test;", conn)
print(df.head())

drop_table = """
    DROP TABLE IF EXISTS test;
    ;
"""

cursor.execute(drop_table)

print("Connection successfully configured.")