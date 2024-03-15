from itertools import groupby
from collections import Counter

def extract(a):
	c = Counter(tuple(l) for _, l in groupby(a))
	return [[tuple(b) for b in a[i:i+2*len(a)].T] for i in range(0, len(a), 2*len(a))]
