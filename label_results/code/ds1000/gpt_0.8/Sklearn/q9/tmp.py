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
from sklearn.calibration import CalibratedClassifierCV

# Create the calibrated classifier
calibrated_clf = CalibratedClassifierCV(svmmodel, cv=5)

# Fit the calibrated classifier on the training data
calibrated_clf.fit(X, y)

# Get the probability estimates for the test data
proba = calibrated_clf.predict_proba(x_test)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
