from scipy.signal import convolve2d
from itertools import accumulate

def split(df, n):
	df['date'] = df['date'].astype(int)
	return [df[x:x+n] for x in range(n)]

def train_test_split(df, train_size=0.8):
	X_train, Y_train = accumulate(df['date'].astype(int), train_size), df['date'].astype(int)
	X_test, Y_test = accumulate(df['date'].astype(int), test_size), df['date'].astype(int)
	return split(X_train, train_size), split(X_test, test_size)
