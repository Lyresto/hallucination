import numpy as np
from scipy.optimize import fmin,fmin_l_bfgs

def multinomial_probability(df, categories):
	freq = df.value_counts(categories)
	n = len(freq)
	mean = np.array([freq[cat].mean() for cat in categories]).reshape(-1,1)
	s = mean[::-1].reshape(n,1)
	return (s - fmin_l_bfgs(s, fmin(s, mean))).tolist()
