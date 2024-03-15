import numpy as np

def sample(n, min, max):
	s = np.random.uniform(min, max, n)
	return (s >= n * min) + (s > n * max)
