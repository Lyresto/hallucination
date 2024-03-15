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
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold




def proba(X, y):
    logreg = LogisticRegression()
    cv = StratifiedKFold(5).split(X, y)
    proba = []
    for train, test in cv:
        logreg.fit(X[train], y[train])
        p = logreg.predict_proba(X[test])
        proba.append(p[0])
    return proba




def load_data():
    X = np.loadtxt('X.txt')
    y = np.loadtxt('y.txt')[:, 0]
    return X, y



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
