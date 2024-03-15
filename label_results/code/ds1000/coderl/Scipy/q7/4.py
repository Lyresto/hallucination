import scipy.stats
from scipy.stats import zscore as z_score, pvalue as p_value
def mean_and_sigma(z_scores):
	mean = sum(z_scores)/len(z_scores)
	sigma = sum((z-mean)**2 for z in z_scores)
	return mean, sigma
