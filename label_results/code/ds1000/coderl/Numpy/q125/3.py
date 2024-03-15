import numpy as np
from statistics import mean

def mean_bin(n, data, k):
	c = np.ceil(n / k)
	return [mean(np.split(data, c)) for _ in range(k)]
