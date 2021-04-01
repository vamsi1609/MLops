import yaml
import os
import json
import joblib
import numpy as np
from src.get_data import read_params


params_path = "params.yaml"
schema_path = os.path.join("prediction_service", "schema_in.json")


class NotInRange(Exception):
    def __init__(self, message="Values entered are not in expected range"):
        self.message = message
        super().__init__(self.message)


def predict(data):
    config = read_params(params_path)
    model_dir_path = os.path.join(
        "prediction_service", "model", "model.joblib")
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    return prediction[0]


def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
    except Exception as e:
        print(e)
        error = {"error": e}
        return error


def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def check_(data):
    schema = get_schema()
    i = 0
    for col,val in schema.items():
        if val["min"] <= data[0][i] <= val["max"]:
            pass
        else:
            raise NotInRange
        i+=1
    return data