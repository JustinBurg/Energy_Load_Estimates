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

@app.route("/")
def hello_world():
    return "Hello, this is the app for Energy Load Estimates.\n"

building_parameters = []

# @app.route('/building_parameters', methods=['POST'])
# def receive_building_parameters():
#     building_parameters.append(request.get_json())
#     #return '', 204
#     return jsonify(building_parameters[-1])

@app.route('/get_estimates', methods=['POST'])
def predict_loads():
    building_parameters.append(request.get_json())
    new_data = np.asarray(list(building_parameters[-1].values())).reshape(1,-1)
    loaded_model = joblib.load("multi_output_model.sav")
    loads = ['Heating','Cooling']
    pred_values = loaded_model.predict(new_data).tolist()[0] 
    response_to_api_call = dict(zip(loads, pred_values))
    return jsonify(response_to_api_call)

if __name__=="__main__":
    app.run(port=5000, host='0.0.0.0',debug=True)
