import scipy.stats
def stats_gaussian_kruskal(z_scores, mu, sigma):
	log_z_scores = np.log(z_scores)
	mean = mean(z_scores)
	sigma = sigma(z_scores)
	f = scipy.stats.gaussian_kruskal
	return f(log_z_scores, mean, sigma).pvalue
