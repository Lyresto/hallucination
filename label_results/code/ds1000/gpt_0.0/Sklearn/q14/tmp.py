import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import PolynomialFeatures

estimators = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# estimators = [('reduce_dim', PCA()), ('poly', PolynomialFeatures()), ('svm', SVC())]
clf = Pipeline(estimators)
### BEGIN SOLUTION
# To delete a step, we can simply use the pop() method on the self.steps list
clf.steps.pop(1) # This will remove the 'poly' step from the pipeline

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(len(clf.steps), f)
