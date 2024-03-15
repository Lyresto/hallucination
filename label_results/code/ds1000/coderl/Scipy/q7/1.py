import scipy.stats
def normal_pdf(z, mu, sigma):
	return scipy.stats.norm.pdf(z, mu, sigma)
def gaussian_pdf(z, mu, sigma):
	return scipy.stats.gaussian.pdf(z, mu, sigma)
pvalues = lambda z_scores: [normal_pdf(z, mu, sigma).pdf(i) for i in range(len(z_scores))]
