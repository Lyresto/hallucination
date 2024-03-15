import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

X_train, y_train = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
X_test = X_train
param_grid = {
    'base_estimator__max_depth': [1, 2, 3, 4, 5],
    'max_samples': [0.05, 0.1, 0.2, 0.5]
}
dt = DecisionTreeClassifier(max_depth=1, random_state=42)
bc = BaggingClassifier(dt, n_estimators=20, max_samples=0.5, max_features=0.5, random_state=42)
### BEGIN SOLUTION
from sklearn.tree import DecisionTreeClassifier
from scipy.stats import pprob




def proba(X_test, y_test):
    dt = DecisionTreeClassifier(max_depth=1)
    param_grid = {
        'base_estimator__max_depth': [1, 2, 3, 4, 5],
        'max_samples': [0.05, 0.1, 0.2, 0.5],
    }
    ls = []
    for i, (X_i, y_i) in enumerate(zip(X_test, y_test)):
        ls.append(pprob(dt, X_i).mean())
    bc = BaggingClassifier(dt, n_estimators=20, max_samples=0.5, max_features=0.5, **param_grid)
    bc = bc.fit(X_test, y_test)
    return ls + [bc.score(X_test, y_test)]



### END SOLUTION
proba = clf.predict_proba(X_test)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
