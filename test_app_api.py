import requests

url = "http://localhost:8000/predict"
data = {"texts": ["This is a positive sentence.", "This is negative."]}

response = requests.post(url, json=data)
print(response.json())

