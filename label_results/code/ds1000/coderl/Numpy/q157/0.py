from itertools import zip_longest

def dist(a, b):
	return sum(b[i][j] - a[i][j] for i in range(len(a)) for j in range(len(a[i])))**0.5

def permutate(arrays):
	return list(zip_longest(*arrays, fillvalue=0))
