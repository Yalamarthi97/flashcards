import os
import psycopg2
import logging
from .decorators import use_cursor, do_in_transaction
from sqlalchemy import create_engine




class PostgresDriver:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.environ["POSTGRES_DATABASE"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_DATABASE_HOST"],
            port=os.environ["POSTGRES_PORT"],
        )

        self.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        

    @use_cursor
    @do_in_transaction
    def execute_fetch_query_single_value(self,query,cursor):
        try:
            cursor.execute(query)
            response = cursor.fetchone()
            return response[0],None
        except Exception as e:
            logging.error("Encountered error when fetching data from db -> "+str(e))
            return None,"Failed to fetch data"
    
    @use_cursor
    @do_in_transaction
    def execute_fetch_query_single_row(self,query,cursor):
        try:
            cursor.execute(query)
            response = cursor.fetchone()
            return response,None
        except Exception as e:
            logging.error("Encountered error when fetching data from db -> "+str(e))
            return None,"Failed to fetch data"
        
    @use_cursor
    @do_in_transaction
    def execute_query(self,query,cursor):
        try:
            cursor.execute(query)
            return None
        except Exception as e:
            logging.error("Encountered error when fetching data from db -> "+str(e))
            return "Failed to execute query"
        
psql_instance = None

def get_instance():
    global psql_instance
    if psql_instance is None:
        psql_instance = PostgresDriver()

    return psql_instance
