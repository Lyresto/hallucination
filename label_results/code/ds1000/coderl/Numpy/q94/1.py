from itertools import groupby


def extract(a):
	xs = list(zip(*a))
	r = []
	for (i, j), (i1, j1) in groupby(enumerate(a), key=lambda x: x[0]):
		xs1 = []
		for k in range(2):
			xs1 += [list(j1[k::2 * k] + j1[k * 2::2 * k])]
		xs.append(xs1)
	return xs
