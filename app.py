from flask import Flask, render_template, request, jsonify
import os
from src.get_data import read_params
import yaml
import joblib
import numpy as np

params_path = "params.yaml"
webapp_root = "webapp"

static_path = os.path.join(webapp_root, "static")
template_path = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_path, template_folder=template_path)


def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
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
         error = {"error": "Something went wrong!!! Please try again"}
         return error    



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data = dict(request.form).values()
                data = [list(map(float,data))]
                response = predict(data)
                return render_template("index.html", response=response)
            elif request.json:
                response= api_response(request)
                return jsonify(response)
        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!!! Please try again"}
            return render_template("404.html", error=error)
        pass
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
