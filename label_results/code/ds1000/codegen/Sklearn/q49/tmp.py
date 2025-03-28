import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier

X_train, y_train = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
X_train[0] = ['a'] * 40 + ['b'] * 40
### BEGIN SOLUTION
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
import pandas

#
### END SOLUTION
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train, y_train)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(X_train, f)
