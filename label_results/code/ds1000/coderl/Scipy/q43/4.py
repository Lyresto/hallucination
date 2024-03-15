from numpy import mean, median
def anderson(x1,x2):
	m, k = mean(x1), median(x1)
	n, p = len(x1), mean(x2)
	return k - m == n/p
