from flask.views import MethodView
from flask import request

from common.validations import return_json_response,schema_validation

from .schemas import create_card_schema
from .service import check_card_exists,add_card_to_db,check_valid_data_exists,fetch_one_card
class CardsV1(MethodView):
    @return_json_response
    def get(self):

        data_exists,error=check_valid_data_exists()
        
        if error:
            return {"error":"Unable to read the data","type":"tex"} , 500
        if data_exists:
            return_response,error = fetch_one_card()
            if error:
                return {"error":"Failed to fetch card","type":"text"},500
            return {"message":return_response,"type":"dict"} , 200


    @schema_validation(schema=create_card_schema)
    @return_json_response
    def post(self,request_body):
        if_exists,check_error=check_card_exists(request_body["card_key"],request_body["card_desc"])
        if check_error:
            return {"error":"Failed to check if the card is already present","type":"text"} , 500
        if not if_exists:
            error=add_card_to_db(request_body["card_key"],request_body["card_desc"])
            if error:
                return {"error":error,"type":"text"} , 500
            return {"message":"Added card","type":"text"}, 200
        else:
            return {"error":"Card already exists with the same description","type":"tex"} , 400
            
        

        
        
