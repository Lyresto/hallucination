from itertools import groupby

def load_data():
	t = [float(x) for x in input().split()]
	idx = [0] * len(t)
	for k,g in groupby(t):
		arr = [x for x,_ in g]
		idx[k] = idx[k-1] + arr.index(k)
	return tuple(t), idx
