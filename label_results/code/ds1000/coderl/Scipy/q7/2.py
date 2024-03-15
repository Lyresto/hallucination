import scipy.stats
import math

def ln_magnitude(z_scores):
	return math.ln(sum(z_scores))

def df(z_scores, mu, sigma):
	return scipy.stats.norm(mu, sigma).pdf(z_scores)

def sc_probability(z_scores, mu, sigma):
	# scipy.stats.norm(mu, sigma).pdf(z_scores)
	df = df(z_scores, mu, sigma)
	l = ln_magnitude(z_scores)
	return df / (l * math.sqrt(2 * math.pi * sigma))
