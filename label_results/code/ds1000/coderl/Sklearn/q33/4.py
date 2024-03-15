from math import exp,sqrt
from collections import defaultdict
from itertools import product

def fit_regressor(y, x):
	d = defaultdict(list)
	for i, xi in enumerate(x):
		d[i].append(y[i])
	for k, v in d.items():
		v.sort()
	return regressor(array([sqrt(xi/yi) for xi, yi in product(x, y)]), x_index=0)
