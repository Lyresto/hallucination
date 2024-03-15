import numpy as np

def stdMeann(df):
	mean = np.mean(df['a'])
	std = np.std(np.array(df['a']))
	return mean, std
