import scipy.stats
def kurtosis(a):
	n, p = len(a), scipy.stats.ks_2samp(a)
	return round(n / p, 1)
