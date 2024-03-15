from itertools import groupby
from numpy import rolling_window

def sliding_window(a):
	l = len(a)
	return [[a[y:y+2*j, x:x+2*j] for j, i in enumerate(list(range(0,l)) + list(range(1,l)))] for x in range(0,l) for y in range(0,l)]
