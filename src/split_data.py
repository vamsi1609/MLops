# Splits the raw data into training and testing
# Puts it into the data\processed folder
import os
import argparse
import pandas as pd 
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_n_save(config_path):
    '''
    Function will split the data into train and test set
    and will save it in data\processed folder
    '''
    config = read_params(config_path)
    # Fetching the configurations
    train_path = config["split_data"]["train_path"]
    test_path = config["split_data"]["test_path"]
    raw_path = config["load_data"]["raw_dataset"]
    test_split = config["split_data"]["test_size"]
    random_state=config["base"]["random_state"]
    #Processing and saving
    print(train_path)
    print(test_path)
    df = pd.read_csv(raw_path, sep=",")
    train,test = train_test_split(df, 
                    test_size=test_split, 
                    random_state=random_state)   
    train.to_csv(train_path, sep=",", index=False)
    test.to_csv(test_path, sep=",", index=False)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_n_save(config_path=parsed_args.config)

