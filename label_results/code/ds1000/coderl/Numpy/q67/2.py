import numpy
def sort_matrices(a):
	a_sorted = sorted(enumerate(a), key=lambda i: a[i][0])
	return [[list(j) for j in zip(*a_sorted)] for i in range(len(a))]
