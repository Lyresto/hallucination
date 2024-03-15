import scipy.stats as stats
def kurtosis(a):
	n = len(a)
	mean = a.mean()
	std = a.std()
	p = stats.t.ppf(n-1, loc=mean, scale=std)
	return round(p, 3)
