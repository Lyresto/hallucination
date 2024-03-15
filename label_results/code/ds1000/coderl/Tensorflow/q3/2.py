import numpy as np
def score(labels,result):
	classes = np.zeros_like(result)
	for i in range(10):
		classes[labels==i] = 1
	return np.sum(classes)/len(classes)
