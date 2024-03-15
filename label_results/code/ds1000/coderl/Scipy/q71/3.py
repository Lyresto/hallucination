import numpy as np
def get_distance_2(y, x):
	mid = np.array([[y[i][j], x[i][j], 0] for i in range(len(y)) for j in range(len(y[i]))])
	return np.dot(mid, mid.T).round()
