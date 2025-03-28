import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

X, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
cv = StratifiedKFold(5).split(X, y)
logreg = LogisticRegression(random_state=42)
### BEGIN SOLUTION
proba = []
for train_index, test_index in cv:
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    logreg.fit(X_train, y_train)
    proba.append(logreg.predict_proba(X_test)[:, 1])



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
