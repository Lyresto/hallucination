import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

X, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
clf = ExtraTreesClassifier(random_state=42)
clf = clf.fit(X, y)
### BEGIN SOLUTION
model = SelectFromModel(clf, prefit=True)
selected_features = model.get_support(indices=True)
column_names = X.columns[selected_features]



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(column_names, f)
