import requests

endpoint="http://127.0.0.1:8000/api/"
# endpoint="https://api.coindesk.com/v1/bpi/currentprice.json/"

get_response = requests.get(endpoint,params={"abc":123},json={"product_id":12})
# get_response = requests.get(endpoint, json={"query": "Hello world"}) # HTTP Request
# print(get_response.text)
# print(get_response.json()['message'])
print(get_response.json())
# print(get_response.status_code)