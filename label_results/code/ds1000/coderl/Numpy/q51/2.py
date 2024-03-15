import numpy as np
def f(X = example_X):
	return [list(np.argwhere(X == i))[0] for i in range(X.shape[0])]
