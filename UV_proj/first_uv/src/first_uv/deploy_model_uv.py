from flask import Flask
from flask import request
from flask import jsonify
import pickle

model_file = 'pipeline_v1.bin'
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask(__name__) # give an identity to your web service

@app.route('/predict', methods=['POST'])  ## in order to send the customer information we need to post its data.
def predict():
  customer = request.get_json()  ## web services work best with json frame, So after the user post its data in json format we need to access the body of json.

  X = dv.transform([customer])
  y_pred = model.predict_proba(X)[0, 1]
  prediction = y_pred
  convert = prediction > 0.5

  result = {
      'lead_probability': float(prediction), ## we need to cast numpy float type to python native float type
      'lead': bool(convert),  ## same as the line above, casting the value using bool method
  }

  return jsonify(result)