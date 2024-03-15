import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC

def cross_val_score(model, X, y, cv=5):
	name = str(model)
	mean_score = 0
	for i in range(cv):
		scores = np.array(cross_val_score(model, X, y, cv=i+1))
		mean_score += scores.mean()
	
	return f'Name model: {name}, Mean score: {mean_score:.5f}'
