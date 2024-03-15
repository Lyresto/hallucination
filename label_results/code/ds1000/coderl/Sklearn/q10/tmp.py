import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn import svm

X, y, x_predict = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
model = svm.LinearSVC(random_state=42)
### BEGIN SOLUTION



def proba(X,y,x_predict):
    print(X)
    print(y)
    print(x_predict)
    model=svm.LinearSVC(penalty='l1',C=1)
    proba=[]
    for i in range(len(x_predict)):
        predict=model.predict(x_predict[i])
        proba.append(1/(1+np.exp(-predict)))
    return proba



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
