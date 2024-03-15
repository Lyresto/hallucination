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
Yes, it is possible to insert or delete a step in a sklearn.pipeline.Pipeline object. 

To insert a step, you can use the insert method of the list object returned by the named_steps() method. For example, to insert a PolynomialFeatures step after the PCA step, you can do:

<code>
steps = clf.named_steps
steps.insert(1, ('poly', PolynomialFeatures()))

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(len(clf.steps), f)
