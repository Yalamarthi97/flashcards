from common.constants import admin_list_of_fetch_cards_cols

def extract_admin_return_data(data):
    response=[]
    if len(data)>0:
        for row in data:
            inner_response={}
            for val in range(0,len(row)):
                inner_response[admin_list_of_fetch_cards_cols[val]]=row[val]
            response.append(inner_response)
        return response,None , 200
    else:
        return None,"No data",404
