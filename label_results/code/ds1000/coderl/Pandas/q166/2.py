import numpy as np

def stdMeann(df):
	m = np.mean(df['b'])
	n = len(df['b'])
	return np.std(np.array([m] * n))
