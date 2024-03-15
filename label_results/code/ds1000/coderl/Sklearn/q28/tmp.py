import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC

model = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION



def cross_val_score(est, X, y, cv=5):
    names = []
    for i, (train, test) in enumerate(zip(X, y)):
        names.append(str(est))
        scores = []
        for k, v in enumerate(est.coef_):
            scores.append(v * X[:, i].sum() / (len(X[:, i]) - k))
        scores.mean()
        print(f'Name model: {est}, Mean score: {scores.mean()}')
    return names



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(model_name, f)
