import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn.svm as suppmach

X, y, x_test = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
svmmodel=suppmach.LinearSVC(random_state=42)
### BEGIN SOLUTION
from sklearn.svm import LinearSVC




def proba(X,y):
    # Predict on test data:
    pred = LinearSVC(penalty='l1', C=1).predict(X)
    # Convert decision function to probabilities:
    proba = 1 / (1 + np.exp(pred - X))
    return proba




def load_data():
    # Data loading:
    X = np.array(list(zip(X,y)))
    y = np.array(list(zip(X,y)))
    X_test = np.array(list(zip(X_test,[1]*len(X_test))))
    return X,y,X_test



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
