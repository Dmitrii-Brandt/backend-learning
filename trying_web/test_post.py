import requests

url = "http://127.0.0.1:8000/cottages"

new_cottage = {
    "id": 6, 
    "House_Letter": "B", 
    "Beds_num":6, 
    "is_booked": False
    }

response = requests.post(url, json=new_cottage)

print(response.status_code)
print(response.json())