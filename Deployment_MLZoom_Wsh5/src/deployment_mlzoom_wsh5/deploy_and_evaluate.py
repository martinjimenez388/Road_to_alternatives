import requests
 
url = 'http://localhost:9696/predict'
 
customer_id = '7795-cfocw'
client = {
 'gender': 'male',
 'seniorcitizen': 0,
 'partner': 'no',
 'dependents': 'no',
 'tenure': 45,
 'phoneservice': 'no',
 'multiplelines': 'no_phone_service',
 'internetservice': 'dsl',
 'onlinesecurity': 'yes',
 'onlinebackup': 'no',
 'deviceprotection': 'yes',
 'techsupport': 'yes',
 'streamingtv': 'no',
 'streamingmovies': 'no',
 'contract': 'one_year',
 'paperlessbilling': 'no',
 'paymentmethod': 'bank_transfer_(automatic)',
 'monthlycharges': 42.3,
 'totalcharges': 1840.75
}
 
response = requests.post(url, json=client)

print(response.status_code)   # e.g. 200
#response.raise_for_status()   # raises an error if the server returned 4xx or 5xx
#print(response.text)

response_data = response.json()
print(response_data)