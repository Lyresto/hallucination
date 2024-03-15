import numpy as np
from sklearn.pipeline import Pipeline

def select_features(features):
	return np.array([[c for c in x] for x in features]).T.tolist()
