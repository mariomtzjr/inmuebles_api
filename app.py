import json

from flask import Flask

from flask_restful import Resource, Api, reqparse

from utils.utils import get_result_from_args

app = Flask(__name__)
api = Api(app)


class PropertyList(Resource):
    """Definition of Resource Class to list properties

    Args:
        Resource (Type[Resource]): Represents an abstract RESTful resource.
    """
    
    def get(self):
        """Method to get all properties using query parameters
        thrugh endpoint.

        Returns:
            json: Json response with list of properties.
        """
        
        parser = reqparse.RequestParser()
        parser.add_argument('city', location='args')
        parser.add_argument('state', location='args')
        parser.add_argument('year', type=int, location='args')
        parser.add_argument('status', location='args')

        args = parser.parse_args()
        result = get_result_from_args(args)

        properties = [
            {
                "address": row.Property.address,
                "city": row.Property.city,
                "price": row.Property.price,
                "description": row.Property.description,
                "status": row.Status.name,
                "anio_construccion": row.Property.year
            } for row in result.get("result")
        ]

        json_response = {}
        json_response["data"] = {}

        json_response["status"] = result.get("status")   
        json_response["message"] = result.get("message")
        
        if not result.get("status") == 403:
            json_response["data"]["properties"] = properties
        else:
            json_response["message_details"] = result.get("message_details")
            
        return json_response

api.add_resource(PropertyList, '/api/properties')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)