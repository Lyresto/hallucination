import numpy as np

def mean_auc(scores):
	return np.mean(np.argmax(scores, axis=1))
