import config 
import psycopg2 as pg
from psycopg2 import OperationalError

def connect_to_database(host=config.host, port=config.port,database=config.database, 
                            user_name=config.user_name, password=config.password):

    conn = None
    try:
        conn = pg.connect(
            host = host
            , port = port
            , database = database
            , user = user_name
            , password = password
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

    return conn
