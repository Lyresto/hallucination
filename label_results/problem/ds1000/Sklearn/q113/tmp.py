import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np

if os.path.exists("sklearn_model"):
    os.remove("sklearn_model")
def creat():
    import pickle

    fitted_model = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
    return fitted_model
fitted_model = creat()
### BEGIN SOLUTION
Yes, it is possible to train the IsolationForest model once and save it for later use. You can use the joblib library to save and load the trained model.

Here's an example code snippet:

import joblib
from sklearn.ensemble import IsolationForest

# Train the model on your clean data
X_train = ...
clf = IsolationForest(...)
clf.fit(X_train)

# Save the trained model
joblib.dump(clf, 'isolation_forest_model.joblib')

# Load the saved model
clf = joblib.load('isolation_forest_model.joblib')

# Use the loaded model to predict outliers on new data
X_test = ...
y_pred = clf.predict(X_test)

In this example, the trained model is saved to a file named "isolation_forest_model.joblib". You can then load the model from the file using joblib.load() and use it to predict outliers on new data without having to retrain the model.

Note that you should only save the trained model once you are satisfied with its performance on your clean data. If you later collect new data that is significantly different from your clean data, you may need to retrain the model on the new data.
### END SOLUTION
if os.path.exists("sklearn_model") and not os.path.isdir("sklearn_model"):
    import pickle

    with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
        pickle.dump("accept", f)
else:
    import pickle

    with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
        pickle.dump("reject", f)
