import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np

dataset = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
# Splitting dataset into training and testing sets
from sklearn.model_selection import train_test_split

X = dataset.iloc[:, :-1] # all columns except the last one
y = dataset.iloc[:, -1] # only the last column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((x_train, x_test, y_train, y_test), f)
