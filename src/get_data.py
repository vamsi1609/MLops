### Read the parameters
### process the data
### Return the processed data
import os
import yaml
import pandas as pd
import argparse 

def read_params(config_path):
    '''
    takes the config_path as input and 
    returns the loaded yaml file 
    '''
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file) 
    return config
def getData(config_path):
    '''
    Takes the input as config_path and 
    gives the input to the read_params function
    which returns the loaded yaml_file 
    using which this function will create the dataframe
    of the data using pandas
    and returns the dataframe
    '''
    config=read_params(config_path)
    data_path = config["data_source"]["source"]
    df = pd.read_csv(data_path, sep=",", encoding= 'utf-8')
    return df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = getData(config_path=parsed_args.config)
