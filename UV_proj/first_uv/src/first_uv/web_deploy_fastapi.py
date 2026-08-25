import requests
 
url = 'http://localhost:9696/predict'
 
customer_id = 'Homework_5_Q4'
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
 
response = requests.post(url, json=client)

print(response.status_code)   # e.g. 200
#response.raise_for_status()   # raises an error if the server returned 4xx or 5xx
#print(response.text)

response_data = response.json()
print(response_data)