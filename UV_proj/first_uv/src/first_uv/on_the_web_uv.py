import requests
 
url = 'http://localhost:9696/predict'
 
customer_id = 'Homework_5'
customer = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}
 
response = requests.post(url, json=customer)

print(response.status_code)   # e.g. 200
response.raise_for_status()   # raises an error if the server returned 4xx or 5xx

response_data = response.json()
print(response_data)