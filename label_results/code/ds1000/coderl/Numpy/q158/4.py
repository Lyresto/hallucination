from itertools import product
from numpy import sum, mean

def dist2d(x, y):
	return sum(dist(x, j) for j in range(y)), mean(dist(x, j) for j in range(y))

def dist(x, y):
	return sum(dist2d(x, j) for j in range(y))
