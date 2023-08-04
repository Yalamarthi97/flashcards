import time

from drivers.psql_driver import driver as psql_object
from common.constants import list_of_fetch_cards_cols,default_timelimits,admin_list_of_fetch_cards_cols

from .queries import *
from .utils import extract_admin_return_data

psql_instance=psql_object.get_instance()

def check_card_exists(card_key,card_desc):
    query=check_unique_card_value_query(card_key,card_desc)
    response,error=psql_instance.execute_fetch_query_single_value(query)
    return response,error

def check_card_valid(card_id):
    query=check_card_valid_query(card_id)
    response,error=psql_instance.execute_fetch_query_single_value(query)
    return response,error


def add_card_to_db(card_key,card_desc):
    query=insert_card_into_db_query(card_key,card_desc)
    error=psql_instance.execute_query(query)
    if error:
        return "Failed to add card"
    
def check_data_exists():
    query=check_data_exists_query()
    response,error=psql_instance.execute_fetch_query_single_value(query)
    return response,error

def check_valid_data_exists():
    query=check_data_valid_exists_query()
    response,error=psql_instance.execute_fetch_query_single_value(query)
    return response,error

def fetch_one_card():
    query=fetch_one_card_query(int(time.time()))
    db_fetch,error=psql_instance.execute_fetch_query_single_row(query)
    response={}
    if error:
        return {},"Failed to fetch the card from the database"
    if db_fetch:
        for key in range(0,len(db_fetch)):
            response[list_of_fetch_cards_cols[key]]=db_fetch[key]
        return response,None
    else:
        return "You are temporarily done; please come back later to review more words."  ,None

def update_card_desc(card_desc,card_id):
    query=update_card_desc_query(card_desc,card_id)
    error=psql_instance.execute_query(query)
    return error

def check_card_validity_and_update(card_id,answered):
    query=""
    current_stage_query=fetch_current_stage_and_wrong_choice(card_id)
    response,error=psql_instance.execute_fetch_query_single_row(current_stage_query)
    
    """ Fetching current_stage at pos 0 and wrong_choice from pos 1 , This is to prevent jumps from state 0 to 10 from requests
     Better way would have been to increment and decrement the values but i still need current_stage and wrong_choices
    as i have a time increment """
    if response:
        current_stage=response[0]
        wrong_choice=response[1]
    if error or not response:
        return "Failed to connect to db to get current stage"
   
    if not answered:
        if wrong_choice + 1 == 10:
            query=set_card_to_next_stage_query(card_id,current_stage,10,int(time.time()))
        else:
            query=set_card_to_next_stage_query(card_id,1,wrong_choice+1,int(time.time())+5)
            
    if answered:
        if current_stage+1 == 11:
            query=set_card_to_next_stage_query(card_id,11,wrong_choice,int(time.time()))
        else:
            query=set_card_to_next_stage_query(card_id,current_stage+1,wrong_choice,int(time.time())+default_timelimits[current_stage])

    error=psql_instance.execute_query(query)
    if error:
        return error
    return None
    
def get_card_or_cards(card_id=None):
    if card_id:
        card_exists_query=check_card_with_id_exists_query(card_id)
        card_exists,error=psql_instance.execute_fetch_query_single_value(card_exists_query)
        if error:
            return None,"Unabled to fetch data" , 500
        if card_exists:
            fetch_card_query=get_cards_query(card_id)
            db_response,error=psql_instance.execute_fetch_query_single_row(fetch_card_query)
            response={}
            if not error:
                for val in range (0,len(db_response)):
                    response[admin_list_of_fetch_cards_cols[val]]=db_response[val]
                return response,None , 200
            else:
                return None,"Unabled to fetch data" , 500
        else:
            return None, " Card with the ID does not exist " , 404
    else:
        fetch_all_cards_query=get_cards_query()
        db_response,error=psql_instance.execute_fetch_query_for_all_data(fetch_all_cards_query)
        response=[]
        if not error:
                return_response,error,code=extract_admin_return_data(db_response)
                return return_response,error,code
        else:
                return None,"Unabled to fetch data" , 500
    
def get_success_or_failed_cards(failed=None):
    db_response_query=get_success_or_failed_cards_query(failed)
    db_response,error=psql_instance.execute_fetch_query_for_all_data(db_response_query)
    if not error:
        return_response,error,code=extract_admin_return_data(db_response)
        return return_response,error,code
    else:
        return None,"Unabled to fetch data" , 500
    
def reset_all_or_one_cards(card_id=None):
    reset_time=int(time.time())
    if card_id:
        query=reset_card_or_cards_query(reset_time,card_id)
        response="Reset the card"
    else:
        query=reset_card_or_cards_query(reset_time)
        response="Reset all cards"
    error=psql_instance.execute_query(query)
    if error:
            return None,error
    
    return response,None
    