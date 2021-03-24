### Loading the data from the data source
### Saving it in the data\raw folder for preprocessing
import os
from get_data import read_params, getData
import argparse

def load_n_save(config_path):
    '''
    loads the data from the config_path using the 
    functions from get_data.py file
    and saves to the data folder
    '''
    config = read_params(config_path)
    df = getData(config_path)
    # a liitle preprocessing for changing the name of the columns
    # because the names have spaces between them which can cause issues 
    # in the future
    up_cols = [col.replace(" ","_") for col in df.columns] 
    raw_path = config["load_data"]["raw_dataset"]
    df.to_csv(raw_path, sep=",", index=False, header=up_cols) 

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_n_save(config_path=parsed_args.config)
