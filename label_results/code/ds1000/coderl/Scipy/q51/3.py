def kurtosis(a):
	n = len(a)
	S = sum(a)
	p = scipy.stats.norm(scale=1)
	k = p.kurtosis(S)
	return (k, p.cdf(k))
