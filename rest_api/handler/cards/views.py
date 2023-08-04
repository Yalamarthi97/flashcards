from flask.views import MethodView
from flask import request

from common.validations import return_json_response,schema_validation

from .schemas import create_card_schema,update_card_desc_schema,update_card_state_schema
from .service import *
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
            return {"message":return_response,"type":"text"} , 200
        else:
            db_not_empty,error = check_data_exists()
            if error:
                return {"error":"Failed to fetch card","type":"text"},500
            if db_not_empty:
                return {"message":"You have no more words to review; you are permanently done!","type":"text"} , 200
            else:
                return {"error":"There is no data in the data base","type":"text"} , 404


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
            
        
    @schema_validation(schema=update_card_state_schema)
    @return_json_response
    def patch(self,request_body):
        card_id=request_body["id"]
        card_valid,error=check_card_valid(card_id)
        if card_valid:
            if str(request_body["answered"]) == "True" or str(request_body["answered"])=="true":
                answered=True
            else:
                answered=False
            
            error=check_card_validity_and_update(card_id,answered)
            if error:
                return {"error":"Failed to save card","type":"text"} , 500
            return {"message":"Updated the card state","type":"text"} , 200
        else:
            return {"message":"Card with this id is either complete or marked as forgotten , try resetting it","type":"text"} , 200
        

class AdminCards(MethodView):
    @return_json_response
    def get(self):
        response,error,code=get_card_or_cards(request.args.get('card_id'))
        if error:
            return {"error":error,"type":"text"} , code
        return {"message":response,"type":"text"} , code


    @return_json_response
    def delete(self):
        check_cards_data_exists,error=check_data_exists()
        if error:
            return {"error":"Failed to check if data exists","type":"text"} , 500
        if check_cards_data_exists:
                response,error=reset_all_or_one_cards(request.args.get('card_id'))
                if not error:
                    return {"message":response,"type":"text"} , 200
                else:
                    return {"error":error,"type":"text"},500  
        else:
            return {"error":"No data present to reset","type":"text"} , 404
    
    @return_json_response
    @schema_validation(schema=update_card_desc_schema)
    def patch(self,request_body):
        if request_body["card_desc"]:
            card_exists,check_error=check_card_exists(request_body["card_key"],request_body["card_desc"])
            
            if check_error:
                return {"error":"Failed to update card","type":"text"} , 500
            if not card_exists:
                error=update_card_desc(request_body["card_desc"],request_body["id"])
                if not error:
                    return {"message":"Updated the description of the card ","type":"text"} , 200
                else:
                    return {"error":"Failed to update card","type":"text"} , 500
            else:
                return {"error":"Failed to update card as the pair of key and  description already exists","type":"text"} , 400


class AdminFailedCards(MethodView):
    @return_json_response
    def get(self):
        response,error,code=get_success_or_failed_cards(True)
        if error:
            return {"error":error,"type":"text"} , code
        return {"message":response,"type":"text"} , code
    
class AdminSuccessfullCards(MethodView):
    @return_json_response
    def get(self):
        response,error,code=get_success_or_failed_cards(False)
        if error:
            return {"error":error,"type":"text"} , code
        return {"message":response,"type":"text"} , code
    