from itertools import product
def dist(x,y):
	d = [[i[j][k] for i in x] for j in range(3)]
	d = list(product(*d))
	return d
