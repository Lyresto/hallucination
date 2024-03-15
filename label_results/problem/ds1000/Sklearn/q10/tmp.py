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
from sklearn.calibration import CalibratedClassifierCV
calibrated_model = CalibratedClassifierCV(model, cv=5)
calibrated_model.fit(X, y)
proba = calibrated_model.predict_proba(x_predict)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
