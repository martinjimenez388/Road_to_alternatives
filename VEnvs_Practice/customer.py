from flask import Flask
from flask import request
from flask import jsonify
import pickle

model_file = 'model_LogReg_CourseLeadScoring.bin'
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask(__name__) # give an identity to your web service

#def predecir(customer, dv, model):
#    X = dv.transform([customer])
#    y_pred = model.predict_proba(X)[0, 1]
#    return y_pred

@app.route('/predict', methods=['POST'])  ## in order to send the customer information we need to post its data.
def predict():
  customer = request.get_json()  ## web services work best with json frame, So after the user post its data in json format we need to access the body of json.

  X = dv.transform([customer])
  y_pred = model.predict_proba(X)[0, 1]
  prediction = y_pred
  convert = prediction > 0.5

  result = {
      'converted_probability': float(prediction), ## we need to cast numpy float type to python native float type
      'converted': bool(convert),  ## same as the line above, casting the value using bool method
  }

  return jsonify(result)  ## send back the data in json format to the user

#Force this code to run only when the file is executed directly, not when imported as a module
# If you run the app through some production server, keep the following lines commented out, as the production server will handle the execution of the app.
#if __name__ == "__main__":
#    app.run(debug=True, host='0.0.0.0', port=9696)