import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

features_dataframe = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
train_size = 0.8
train_index = int(len(features_dataframe) * train_size)
train_dataframe = features_dataframe[:train_index]
test_dataframe = features_dataframe[train_index:]



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((train_dataframe, test_dataframe), f)
