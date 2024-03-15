from itertools import chain

def dist(x,y):
	return list(chain.from_iterable(zip(x,y).T))

def pairwise(dists):
	P = list(zip(*dists))
	return list(zip(P[0], P[1]))
