def check_unique_card_value_query(card_key,card_desc):
    return f"""select exists(select 1 from cards where card_key='{card_key}' and card_desc='{card_desc}');"""

def insert_card_into_db_query(card_key,card_desc):
    return f""" insert into cards (card_key,card_desc) values ('{card_key}','{card_desc}');"""