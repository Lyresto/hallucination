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
from sklearn.ensemble import IsolationForest
import joblib

# Fit the model to your clean data
model = IsolationForest()
model.fit(X_train)

# Save the fitted model to a file
joblib.dump(model, "sklearn_model.pkl")


### END SOLUTION
if os.path.exists("sklearn_model") and not os.path.isdir("sklearn_model"):
    import pickle

    with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
        pickle.dump("accept", f)
else:
    import pickle

    with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
        pickle.dump("reject", f)
