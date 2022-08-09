import requests
r = requests.post('http://127.0.0.1:8000', json={
  "Id": 78912,
  "Customer": "Jason Sweet",
  "Quantity": 1,
  "Price": 18.00
},headers = {'foobar': 'raboof'})
print(f"Status Code: {r.status_code}, Response: {r.json()}")

