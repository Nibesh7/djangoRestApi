import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update" 
data={
    'title':"updated test testing",
    'price':'400.00'
}
get_response = requests.put(endpoint,json=data) # HTTP Request

print(get_response.json())