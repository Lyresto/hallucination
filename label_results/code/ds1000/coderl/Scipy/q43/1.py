from numpy import mean, median
from scipy.stats import anderson

def anderson(x1, x2):
	m, k = mean(x1), median(x1)
	a, b = mean(x2), median(x2)
	return a!= b and k - m < 0.05 * (a - b)
