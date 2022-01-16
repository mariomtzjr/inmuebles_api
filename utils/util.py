import json

from sqlalchemy import text

from database.db import DB
from database.queries import *

db_connection = DB.init_connection_engine()


class DBExecutor(object):

    def get_query(args):
        """Method that returns the query according 
        to the search parameters of the url

        Args:
            args (dict): Query parameters that user setted
            into url to filter search

        Returns:
            string: String with query to execute
        """

        query = None
        status = args.get('status')

        city = args.get('city')
        state = args.get('state')
        year = args.get('year')

        valid_status = ["en_venta", "vendido", "pre_venta"]

        if status in valid_status:
            if city is not None and (year is None and state is None):
                print(f"City: {city}")
                query = CITY_QUERY.format(city)
            elif year is not None and (city is None and state is None):
                print(f"Year: {year}")
                query = YEAR_QUERY.format(year)
            elif city is not None and (year is not None and state is None):
                print(f"City: {city} Year:{year}")
                query = CITY_YEAR_QUERY.format(city, year)
            elif city is not None and (year is not None and state is not None):
                print(f"City: {city} Year:{year} State:{state}")
                query = CITY_YEAR_STATE_QUERY.format(city, year, state)
            elif city is not None and (state is not None):
                print(f"City: {city} State:{state}")
                query = CITY_STATE_QUERY.format(city, state)
            else:
                print(f"Status: {status}")
                query = STATUS_QUERY.format(status)
            return query
    
    def execute_query(query):
        """[summary]

        Args:
            query (string): Query to be executed

        Returns:
            array: List of properties with certain criteria
        """

        try:
            with db_connection.connect() as connection:

                result = connection.execute(text(query))
                response = build_response(result)
            return response
        except Exception as e:
            print("Error executing query\n")
            print(e)
            result = ""
            response = {}
            response["status"] = 403
            response["result"] = result
            response["message"] = "BAD REQUEST"
            response["message_details"] = "Some parameters are not valid."

            return response


def build_response(result):
    response = {}
    response["result"] = None

    response["status"] = 200
    response["message"] = "OK"
    response["result"] = result
    

    return response