import numpy as np
def solve(features):
	# features = np.array(features)
	# print(features)
	n_gen = np.array([len(s) for s in features])
	return np.array([[1 if n_gen[i]==i else 0 for i in range(len(s))] for s in features]).T
