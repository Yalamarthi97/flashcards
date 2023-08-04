def check_unique_card_value_query(card_key,card_desc):
    return f"""select exists(select 1 from cards where card_key='{card_key}' and card_desc='{card_desc}');"""

def insert_card_into_db_query(card_key,card_desc):
    return f""" insert into cards (card_key,card_desc) values ('{card_key}','{card_desc}');"""

def check_data_valid_exists_query():
    return f""" select exists ( select 1 from cards where hidden = false);"""

def check_data_exists_query():
    return f""" select exists ( select 1 from cards );"""


def fetch_one_card_query(current_timestamp):
    return f"""select id,card_key,card_desc,up_in,current_stage,wrong_choices from cards where current_stage = 0 and hidden = false union select id,card_key,card_desc,up_in,current_stage,wrong_choices from cards where up_in < {current_timestamp} and hidden = false order by current_stage desc limit 1"""

def update_card_desc_query(card_desc,card_id):
    return f"""update  cards set card_desc ='{card_desc}' where id={card_id};"""

def set_card_to_next_stage_query(card_id,current_stage,wrong_choices,up_in):
    if wrong_choices == 10 or current_stage == 11:
        return f"""update cards set hidden=true , current_stage={current_stage} , wrong_choices={wrong_choices} where id={card_id} ;  """
    else:
        return f"""update cards set current_stage={current_stage} , wrong_choices={wrong_choices} , up_in ={up_in} where id={card_id};"""
    
def check_card_with_id_exists_query(card_id):
    return f""" select exists ( select 1 from cards where id = {card_id});"""

def get_cards_query(card_id=None):
    if card_id:
        return f"""select id,created_at,up_in,card_key,card_desc,current_stage,wrong_choices,hidden from cards where id={card_id};"""
    else:
        return f"""select id,created_at,up_in,card_key,card_desc,current_stage,wrong_choices,hidden from cards"""

def get_success_or_failed_cards_query(failed=None):
    if failed:
        return f"""select id,created_at,up_in,card_key,card_desc,current_stage,wrong_choices,hidden from cards where hidden = true"""
    else:
          return f"""select id,created_at,up_in,card_key,card_desc,current_stage,wrong_choices,hidden from cards where hidden = true and current_stage=11"""
    
def reset_card_or_cards_query(rollback_time,card_id=None):

    if card_id:
        return f"""update cards set current_stage=0,wrong_choices=0,hidden=false,up_in={rollback_time} where id={card_id} ;"""
    else:
        return f"""update cards set current_stage=0,wrong_choices=0,hidden=false,up_in={rollback_time} ;"""