from conf.db_conf import db_conf
import psycopg2 as pg
from psycopg2 import OperationalError
import pandas.io.sql as psql
from sqlalchemy import create_engine

class DB_Utils:
    """
    A class to contain all PostgreSQL connection and query commands.
    ...

    Attributes
    ----------
    None

    Methods
    -------
    _connect_to_database():
        an internal function to form the connection with the postgresql database
    sql_execute(sql_string):
        uses the connection cursor to execute any SQL command to the database
    sql_read_as_df(sql_string):
        returns a Pandas dataframe from the database based on the sql command passed in
    """

    def __init__(self):
        self.host = db_conf["host"]
        self.port = db_conf["port"]
        self.database = db_conf["database"]
        self.username = db_conf["username"]
        self.password = db_conf["password"]
        self.conn = self._connect_to_database()
        self.cursor = self.conn.cursor()

    def _connect_to_database(self):
        conn = None
        try:
            conn = pg.connect(
                host = self.host
                , port = self.port
                , database = self.database
                , user = self.username
                , password = self.password
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")

        return conn

    def sql_execute(self, sql_string):
        self.cursor.execute(sql_string)
        return None

    def sql_read_as_df(self, sql_string):
        df = psql.read_sql(sql_string, self.conn)
        return df

    def sql_create_table(self, df, sql_table_name, schema=None, if_exists="replace", index=False):
        engine = create_engine(f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}")
        df.to_sql(sql_table_name, con=engine, schema=schema, if_exists=if_exists, index=index)
        return None





