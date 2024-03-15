import numpy as np
import scipy.optimize as sciopt

def fit_multinomial(df, weights):
	n = len(df)
	res = np.array([])
	for i in range(n):
		res[i] = 0
		for j in range(n):
			if df.loc[i,j] == j:
				res[i] += weights[j]
	
	m = np.array([])
	l = np.array([])
	for i in range(n):
		m = np.maximum(m, (weights ** i) / (n - 1))
		l = np.minimum(l, (weights ** i) / (n - 1))
	res = m + l
	return res
	
	
def multinomial_probability(df, x):
	n = len(df)
	res = 0
	for i in range(n):
		res += df.loc[x,i] * (weights ** i)
	return res / (n ** (res.shape[0] - 1))
	
def predict_max_likelihood(df, weights):
	n = len(df)
	res = np.array([])
	for i in range(n):
		res[i] = 0
		for j in range(n):
			if df.loc[i,j] == j:
				res[i] += weights[j]
	
	m = np.array([])
	l = np.array([])
	for i in range(n):
		m = np.maximum(m, (weights ** i) / (n - 1))
		l = np.minimum(l, (weights ** i) / (n - 1))
	
	return m + l
