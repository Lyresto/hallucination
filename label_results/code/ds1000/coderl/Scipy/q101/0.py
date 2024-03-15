from collections import Counter
import numpy as np

def fit_multinomial(df, weights):
	n = len(df)
	
	dist = np.array([[0] * n for i in range(n)])
	
	for i in range(n):
		for j in range(n):
			dist[i][j] = np.sum(df[i == j]) / (df[i].count(j) * weights[j])
	
	res = np.array([dist[i][j] for i in range(n) for j in range(n)])
	
	return res, dist
	
def multinomial_probability(df, weights):
	res, dist = fit_multinomial(df, weights)
	return res
