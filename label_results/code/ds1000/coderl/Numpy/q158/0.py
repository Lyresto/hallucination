import numpy as np
def dist(x, y):
	return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
def dist_pairs(x, y):
	return list(zip(dist(x, y), dist(y,x)))
