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
class Pipeline:

    


def __init__(self, estimators):
    self.estimators = estimators




def named_steps(self):
    return {name: self.steps[name] for name in self.steps}




def __setitem__(self, key, value):
    if key not in self.steps:
        raise ValueError
    self.steps[key] = value




def __getitem__(self, key):
    return self.steps[key]



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(len(clf.steps), f)
