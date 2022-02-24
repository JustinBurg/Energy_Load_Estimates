from flask import Flask, request
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import joblib
import json
import sys

app = Flask(__name__)

from flask import Flask, jsonify, request

app = Flask(__name__)

def load_tester(file):
    with open(file) as f:
        data = json.load(f)
    return np.asarray(list(data.values())).reshape(1,-1)  

@app.route("/")
def hello_world():
    return "Hello, Justin!"

load_estimate_inputs = []

@app.route('/loads', methods=['POST'])
def receive_loads():
    load_estimate_inputs.append(request.get_json())
    return '', 204

@app.route('/loads')
def list_metrics():
    return jsonify(load_estimate_inputs)

@app.route('/load_estimates', methods=['POST'])
def predict_loads(json_file):
    new_data = load_tester(json_file)
    loaded_model = joblib.load("multi_output_model.sav")
    loads = ['Heating','Cooling']
    pred_values = loaded_model.predict(new_data).tolist()[0] 
    response_to_api_call = dict(zip(loads, pred_values))
    print(response_to_api_call)

if __name__=="__main__":
    app.run(port=5000, debug=True)
