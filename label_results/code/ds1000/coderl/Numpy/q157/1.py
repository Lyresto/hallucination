import numpy as np

def dist(p, q):
	x, y = p[0], p[1]
	z = q[0]
	w = q[1]
	d = np.sqrt((x**2 + y**2)**2 - (z**2 + w**2)**2)
	return d

def pairs(dists):
	pairs = []
	for i in range(len(dists)):
		pairs.append([dists[i][0], dists[i][1]])
		pairs.append([dists[i][2], dists[i][0]])
	return pairs
