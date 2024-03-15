z_scores = np.random.normal(mu, sigma, len(z_scores))
p_values = scipy.stats.norm.sf(z_scores)
