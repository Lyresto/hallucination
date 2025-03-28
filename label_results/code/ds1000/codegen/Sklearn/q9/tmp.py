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
svmmodel=suppmach.LinearSVC(C=1)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(proba, f)
