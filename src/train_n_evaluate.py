### Loading the train and test data 
### Training the model
### Saving the metrics and parameters 

import os
import warnings
import sys
import numpy as np
import pandas as pd 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_params
import argparse
import joblib
import json

def get_metrics(ypred,ytest):
    mse = mean_squared_error(ypred, ytest)
    mae= mean_absolute_error(ypred, ytest)
    r2 = r2_score(ytest, ypred)
    return mae, mse, r2
def train_n_evaluate(config_path):
    config = read_params(config_path)
    train_path= config["split_data"]["train_path"]
    test_path=config["split_data"]["test_path"]
    random_state=config["base"]["random_state"]
    model_dir=config["model_dir"]
    alpha= config["estimators"]["Elastic_Net"]["params"]["alpha"]
    l1_ratio= config["estimators"]["Elastic_Net"]["params"]["l1_ratio"]

    target = config["base"]["target_col"]


    train_data=pd.read_csv(train_path, sep=",")
    test_data=pd.read_csv(train_path, sep=",")
    y_train = train_data.drop(target, axis=1)
    y_test = test_data.drop(target, axis=1)

    model = ElasticNet(alpha= alpha, l1_ratio= l1_ratio, random_state= random_state)
    
    model.fit(train_data, y_train)

    y_pred = model.predict(test_data)
    (mae, mse, r2)= get_metrics(y_pred,y_test)

    params_file= config["reports"]["params"]
    scores_file= config["reports"]["scores"]
    
    with open (scores_file,"w") as f:
        scores = {
            'mse': mse,
            'mae': mae,
            'r2': r2
        }
        json.dump(scores, f, indent=4)

    with open(params_file, "w") as f:
        params={
            'alpha': alpha,
            'l1_ratio': l1_ratio
        }
        json.dump(params, f, indent=4)

    print(f"ElasticNet model(aplha={alpha}, l1_ratio={l1_ratio})")
    print(f"MSE: {mse}")
    print(f"MAE: {mae}")
    print(f"R2: {r2}")

    os.makedirs(model_dir, exist_ok=True)
    model_path= os.path.join(model_dir,"model.joblib")

    joblib.dump(model, model_path)




if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_n_evaluate(config_path=parsed_args.config)
