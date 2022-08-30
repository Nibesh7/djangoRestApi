import requests
product_id = input("Enter the id to delete the product\n")
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid id')
print(product_id)
if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete" 
    get_response = requests.delete(endpoint) # HTTP Request

    print(get_response.status_code)