import numpy as np
import pandas

def load_data():
	X = []
	Y = []
	for i in range(0, 40):
		X.append([i] * 40 + ['a'] * 40 + [i] * 40)
	for i in range(0, 40):
		X[i][i] = int(np.mean(X[i][:40]))
	for i in range(0, 40):
		Y.append([i] * 40 + ['a'] * 40 + [i] * 40)
	X = pandas.DataFrame(X)
	Y = pandas.DataFrame(Y)
	return (X, Y)
