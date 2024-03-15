from itertools import chain, groupby
from numpy import array, sqrt, floor, ceil, copysign
from operator import mul

def load_data():
	t = array(list(map(float, input().split())))
	idx = list(chain.from_iterable([i-1 for i,_ in groupby(t)]))
	return t, idx
