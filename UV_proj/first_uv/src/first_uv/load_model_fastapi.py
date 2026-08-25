from fastapi import FastAPI
from pydantic import BaseModel
import pickle

model_file = 'pipeline_v1.bin'
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI() # give an identity to your web service

class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post('/predict')  ## in order to send the customer information we need to post its data.
def predict(data: Client):

  client = data.model_dump()
  X = dv.transform([client])
  y_pred = model.predict_proba(X)[0, 1]
  prediction = y_pred
  convert = prediction > 0.5

  result = {
      'lead_probability': float(prediction), ## we need to cast numpy float type to python native float type
      'lead': bool(convert),  ## same as the line above, casting the value using bool method
  }

  return result