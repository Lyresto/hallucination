from itertools import combinations

def get_max_set(a):
	V = np.vectorize(tuple)
	X = list(zip(*a))
	Z = list(zip(*X))
	U, V = list(zip(*sorted(set(X) - set(Y) for Y in V))))
	return [[tuple(v) for v in z] for z in U]
