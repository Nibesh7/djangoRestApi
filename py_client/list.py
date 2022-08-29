from lib2to3.pgen2 import token
import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/" 
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username':'nibesh','password':password}) # HTTP Request
# print(auth_response.json(),auth_response.status_code)

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    print("token=" + token)
    headers={
        "Authorization":f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/" 

    get_response = requests.get(endpoint, headers=headers) # HTTP Request
    # print(get_response)
    print(get_response.json())