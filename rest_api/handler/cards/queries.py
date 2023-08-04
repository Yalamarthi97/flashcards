def check_unique_card_value_query(card_key,card_desc):
    return f"""select exists(select 1 from cards where card_key='{card_key}' and card_desc='{card_desc}');"""

def insert_card_into_db_query(card_key,card_desc):
    return f""" insert into cards (card_key,card_desc) values ('{card_key}','{card_desc}');"""

def check_data_valid_exists_query():
    return f""" select exists ( select 1 from cards where hidden = false);"""

def fetch_one_card_query(current_timestamp):
    return f"""select id,card_key,card_desc,up_in,current_stage,wrong_choices from cards where current_stage = 0 and hidden = false union select id,card_key,card_desc,up_in,current_stage,wrong_choices from cards where up_in < {current_timestamp} and hidden = false order by current_stage limit 1"""