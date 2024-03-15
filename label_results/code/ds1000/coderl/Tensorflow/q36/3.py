import numpy as np

def mean_score(scores):
	return np.mean(np.argmax(scores, axis=1))
