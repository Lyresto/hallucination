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
# Find the index to split the data into train and test sets
split_index = int(len(features_dataframe) * 0.8)

# Split the data into train and test sets
train_dataframe = features_dataframe.iloc[:split_index]
test_dataframe = features_dataframe.iloc[split_index:]

# Make sure the test set is older than the train set
if test_dataframe.iloc[0]["date"] < train_dataframe.iloc[-1]["date"]:
    train_dataframe = pd.concat([train_dataframe, test_dataframe.iloc[:-1]])
    test_dataframe = test_dataframe.iloc[-1:]

# Sort the dataframes by date
train_dataframe = train_dataframe.sort_values(by=["date"])
test_dataframe = test_dataframe.sort_values(by=["date"])

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((train_dataframe, test_dataframe), f)
