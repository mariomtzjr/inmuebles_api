import json

from sqlalchemy.orm import Session, sessionmaker

from database.db import DB
from database.models import Property, Status, StatusHistory

db = DB.init_connection_engine()

Session = sessionmaker(bind = db)
session = Session()


def get_result_from_args(args):
    """Returns json result from database using args like filters
    from request args.

    Parameters:
        status: different states that the property has had. Valid status are "pre_venta", "en_venta", "vendido".
        state: Property location
        city: Property location into state
        year: When property was builded

    Returns:
        json: result from database using args like filters from request args.
    """

    response = {}
    response["status"] = 200
    response["message"] = "OK"
    response["result"] = None

    status = args.get('status')

    city = args.get('city')
    state = args.get('state')
    year = args.get('year')

    valid_status = ["en_venta", "vendido", "pre_venta"]

    if status in valid_status:
        if city is not None and (year is None and state is None):
            print(f"City: {city}")
            result = session.query(Property, Status, StatusHistory)\
                .filter(Status.id == StatusHistory.status_id)\
                .filter(Property.id == StatusHistory.property_id)\
                .filter(Status.name==status)\
                .filter(Property.city==city)\
                .filter((Property.city.is_distinct_from(''))\
                        |(Property.address.is_distinct_from(''))\
                        |(Property.year.is_distinct_from('')))\
                .order_by(StatusHistory.update_date.desc())
            response["result"] = result
            return response

        elif year is not None and (city is None and state is None):
            print(f"Year: {year}")
            result = session.query(Property, Status, StatusHistory)\
                .filter(Status.id == StatusHistory.status_id)\
                .filter(Property.id == StatusHistory.property_id)\
                .filter(Status.name==status)\
                .filter(Property.year==year)\
                .filter((Property.city.is_distinct_from(''))\
                        |(Property.address.is_distinct_from(''))\
                        |(Property.year.is_distinct_from('')))\
                .order_by(StatusHistory.update_date.desc())
            response["result"] = result
            return response

        elif city is not None and (year is not None and state is None):
            print(f"City: {city} Year:{year}")
            result = session.query(Property, Status, StatusHistory)\
                .filter(Status.id == StatusHistory.status_id)\
                .filter(Property.id == StatusHistory.property_id)\
                .filter(Status.name==status)\
                .filter((Property.city==city) & (Property.year==year))\
                .filter((Property.city.is_distinct_from(''))\
                        |(Property.address.is_distinct_from(''))\
                        |(Property.year.is_distinct_from('')))\
                .order_by(StatusHistory.update_date.desc())
            response["result"] = result
            return response

        elif city is not None and (year is not None and state is not None):
            print(f"City: {city} Year:{year} State:{state}")
            result = session.query(Property, Status, StatusHistory)\
                .filter(Status.id == StatusHistory.status_id)\
                .filter(Property.id == StatusHistory.property_id)\
                .filter(Status.name==status)\
                .filter((Property.city==city) & (Property.year==year) & (Property.state==state))\
                .filter((Property.city.is_distinct_from(''))\
                        |(Property.address.is_distinct_from(''))\
                        |(Property.year.is_distinct_from('')))\
                .order_by(StatusHistory.update_date.desc())
            response["result"] = result
            return response

        else:
            print(f"Status: {status}")
            result = session.query(Property, Status, StatusHistory)\
                .filter(Status.id == StatusHistory.status_id)\
                .filter(Property.id == StatusHistory.property_id)\
                .filter(Status.name==status)\
                .filter((Property.city.is_distinct_from(''))\
                        |(Property.address.is_distinct_from('')))\
                .order_by(StatusHistory.update_date.desc())
            response["result"] = result
            return response
    
    response = {}
    response["status"] = 403
    response["message"] = "BAD REQUEST"
    response["message_details"] = f"status='{status}' not valid."
    response["result"] = ""

    return response
