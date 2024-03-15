from math import ceil, log

def f(img):
	return ceil(log(sum(sum(img[i, j] > threshold * threshold for j in range(512)), 2.0)) / log(2.0, 10))
