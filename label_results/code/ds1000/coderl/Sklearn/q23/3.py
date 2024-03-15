import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold

def proba(y, X):
	lgr = LogisticRegression()
	lgr.fit(X, y)
	scores = lgr.predict_proba(np.array(X))
	return scores

def load_data():
	#your code here
	X = np.array(pd.read_csv("input.csv"))[:, :2]
	Y = np.array(pd.read_csv("input.csv")[:, :2])
	return X, Y
