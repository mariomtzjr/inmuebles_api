import os

import sqlalchemy
import pymysql.cursors

class DB(object):
    uri = None
    base = None
    engine = None
    session = None

    def init_connection_engine():
        """This function starts database connection.
        Returns a database connection pool

        parameters:
            - username: Allowed user to use the database
            - password: Secure password that user uses
            - host: IP Address of database
            - port: Allowed port which database connection is stablished
            - database: Database name
        """
        
        pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME")

            ),
            pool_size=5,
            max_overflow=2,
            pool_timeout=30,
            pool_recycle=1800
        )

        return pool