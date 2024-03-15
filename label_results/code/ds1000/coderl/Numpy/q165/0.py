from numpy import matrix
from itertools import product

def distance(a):
	return matrix(list(zip(*product(*a))))
