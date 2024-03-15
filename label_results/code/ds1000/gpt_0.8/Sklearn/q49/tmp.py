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

# load data in the example
iris = datasets.load_iris()
X = iris.data[(iris.target==0) | (iris.target==1)]
y = iris.target[(iris.target==0) | (iris.target==1)]

# Class 0 has indices 0-49. Class 1 has indices 50-99.
# Divide data into 80% training, 20% testing.
train_indices = list(range(40)) + list(range(50,90))
test_indices = list(range(40,50)) + list(range(90,100))
X_train = X[train_indices]
X_test = X[test_indices]
y_train = y[train_indices]
y_test = y[test_indices]

# Convert X_train to a pandas DataFrame
X_train = pd.DataFrame(X_train)

# Insert fake categorical variable
X_train['category'] = ['a']*40 + ['b']*40

# One-hot encode the categorical variable
X_train_encoded = pd.get_dummies(X_train, columns=['category'])

# Model
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train_encoded, y_train)



### END SOLUTION
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train, y_train)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(X_train, f)
