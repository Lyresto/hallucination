import scipy.stats

def ddnxt(a, b, n):
	return (a + b) / n

def approx_pvalue(z_scores, mu, sigma):
	sigma2 = sigma ** 2
	df = ddnxt(sigma2, sigma2 - mu, len(z_scores) - 1)
	acf = np.cumsum(z_scores) / df
	p_values = scipy.stats.norm.pdf(acf, mu, sigma).round()
	return p_values
