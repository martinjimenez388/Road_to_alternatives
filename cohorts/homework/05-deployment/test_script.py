import pickle

with open('pipeline.bin', 'rb') as f_in:
    pipe = pickle.load(f_in)

customer = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

print("Predicted probability for Q3: ", round(pipe.predict_proba([customer])[0,1], 3))
print("Now, I load the model and call it for the 2nd provided lead.")

import requests
 
url = 'http://localhost:9696/predict'
 
client = {
  "lead_source": "organic_search",
  "industry": "technology",
  "employment_status": "employed",
  "location": "europe",
  "number_of_courses_viewed": 4,
  "annual_income": 80304.0,
  "interaction_count": 7,
  "lead_score": 0.74
}
 
response = requests.post(url, json=client)

print("Status code: ", response.status_code)   # e.g. 200
#response.raise_for_status()   # raises an error if the server returned 4xx or 5xx
#print(response.text)

response_data = response.json()
print(response_data)