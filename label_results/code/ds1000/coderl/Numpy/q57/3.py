import numpy as np

def max_sets(a):
	N = len(a)
	s = set()
	for i in range(N):
		for j in range(N):
			if a[i][j] == 0:
				s.add((i,j))
	return max(s, key = lambda x : len(x[1]))
	


# YOU'VE DOED THIS KATA!
