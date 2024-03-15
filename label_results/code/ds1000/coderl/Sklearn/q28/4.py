import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC

def cross_val_score(model, X, y, cv=5):
	scores = np.mean([cross_val_score(model, X[i], y[i], cv=cv) for i in range(len(X))])
	return f"Name model: {model.__class__.__name__}, Mean score: {scores.mean()}"
