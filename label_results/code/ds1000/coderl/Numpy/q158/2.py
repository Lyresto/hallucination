import numpy as np

def dist_pair(x,y):
	for i,j in zip(x,y):
		yield i,j

def dist(x,y):
	return list(map(lambda x:np.linalg.norm(x)-np.linalg.norm(y), dist_pair(x,y)))
