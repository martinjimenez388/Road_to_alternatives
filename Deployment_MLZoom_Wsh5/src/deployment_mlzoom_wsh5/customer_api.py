from fastapi import FastAPI
from pydantic import BaseModel
import pickle

#Dump the model
model_file = 'LogReg_model.bin'
with open(model_file, 'rb') as f_in:
    pipe = pickle.load(f_in)

#Define the app
app = FastAPI()

#Define the data type of the input variables to be fed to the model
class Client(BaseModel):
    gender:                  str
    seniorcitizen:           int
    partner:                 str
    dependents:              str
    tenure:                  int
    phoneservice:            str
    multiplelines:           str
    internetservice:         str
    onlinesecurity:          str
    onlinebackup:            str
    deviceprotection:        str
    techsupport:             str
    streamingtv:             str
    streamingmovies:         str
    contract:                str
    paperlessbilling:        str
    paymentmethod:           str
    monthlycharges:          float
    totalcharges:            float


@app.post('/predict')
def predict(data):
    customer = data.model_dump()#Extract the data into a dictionary
    y_pred = pipe.predict_proba([customer])[0,1]
    cond = y_pred > 0.5

    result = {
        "The client will churn with a probability of": f"{y_pred*100} %",
        "Churn": cond
    }

    return result