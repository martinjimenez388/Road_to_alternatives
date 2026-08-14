import requests
 
url = 'http://localhost:9696/predict'
 
customer_id = 'xyz-123'
customer = {
  'lead_source': 'paid_ads',
 'industry': 'NA',
 'number_of_courses_viewed': 1,
 'annual_income': 79450.0,
 'employment_status': 'unemployed',
 'location': 'south_america',
 'interaction_count': 4,
 'lead_score': 0.94
}
 
response = requests.post(url, json=customer)

print(response.status_code)   # e.g. 200
response.raise_for_status()   # raises an error if the server returned 4xx or 5xx

response_data = response.json()
print(response_data)

if response_data['converted']:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)
