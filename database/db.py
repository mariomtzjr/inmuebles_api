import os

import sqlalchemy

class DB(object):
    uri = None
    base = None
    engine = None
    session = None

    def init_connection_engine():
        """This function starts database connection.
        Returns a database connection pool

        Returns:
            EngineObject: Connects a Pool and Dialect together to provide a 
            source of database connectivity and behavior.
        """
        
        print("Starting database connection...")
        pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username=os.environ.get("DB_USER"),
                password=os.environ.get("DB_PASSWORD"),
                host=os.environ.get("DB_HOST"),
                port=os.environ.get("DB_PORT"),
                database=os.environ.get("DB_NAME")

            ),
            pool_size=5,
            max_overflow=2,
            pool_timeout=30,
            pool_recycle=1800
        )

        print("DB_USER: ", os.environ.get("DB_USER"))
        print("DB_HOST: ", os.environ.get("DB_HOST"))
        print("DB_NAME: ", os.environ.get("DB_NAME"))
        return pool