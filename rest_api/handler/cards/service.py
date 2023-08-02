from drivers.psql_driver import driver as psql_object

from .queries import check_unique_card_value_query,insert_card_into_db_query
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
