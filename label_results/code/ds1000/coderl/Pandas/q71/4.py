import numpy as np

def f(df, columns=['b', 'e']):
	a, b, c = df.drop(columns=['a', 'b', 'c'], axis=1)
	return np.concatenate([a[c] for c in columns], axis=1).sum(axis=1)
