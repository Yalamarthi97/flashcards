import time

from drivers.psql_driver import driver as psql_object
from common.constants import list_of_fetch_cards_cols

from .queries import check_unique_card_value_query,insert_card_into_db_query,check_data_valid_exists_query,fetch_one_card_query
psql_instance=psql_object.get_instance()

def check_card_exists(card_key,card_desc):
    query=check_unique_card_value_query(card_key,card_desc)
    response,error=psql_instance.execute_fetch_query_single_value(query)
    return response,error

def add_card_to_db(card_key,card_desc):
    query=insert_card_into_db_query(card_key,card_desc)
    error=psql_instance.execute_query(query)
    if error:
        return "Failed to add card"

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

    for key in range(0,len(db_fetch)):
        response[list_of_fetch_cards_cols[key]]=db_fetch[key]
    return response,None
