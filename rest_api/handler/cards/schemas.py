create_card_schema ={
    "type":"object",
    "properties":{
        "card_key":{"type":"string"},
        "card_desc":{"type":"string"},
    },
    "required":["card_key","card_desc"]
}

update_card_schema={
    "type":"object",
    "properties":{
        "card_desc":{"type":"string"},
        "card_key":{"type":"string"},
        "id":{"type":"number"},
        "wrong_choices":{"type":"number"},
        "current_stage":{"type":"number"},
        "answered":{"type":"string"},
    },
    "required":["id","wrong_choices","current_stage","answered","card_key"]
}