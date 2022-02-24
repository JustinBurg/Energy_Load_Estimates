import pandas as pd
import numpy as np
import joblib
import json
import sys

def load_tester(file):
    with open(file) as f:
        data = json.load(f)
    return np.asarray(list(data.values())).reshape(1,-1)  


def predict_loads(json_file):
    new_data = load_tester(json_file)
    loaded_model = joblib.load("multi_output_model.sav")
    loads = ['Heating','Cooling']
    pred_values = loaded_model.predict(new_data).tolist()[0] 
    response_to_api_call = dict(zip(loads, pred_values))
    print(response_to_api_call)

new_data = sys.argv[1]
predict_loads(new_data)
