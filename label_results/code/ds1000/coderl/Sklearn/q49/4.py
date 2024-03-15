from sklearn.base import Transformer
from numpy import array
import pandas


def encode_columns(s):
	return array([[v] if type(v)!=str else [float(v)] for v in s], dtype=object)


def encode_dataframe(s):
	return pandas.DataFrame(encode_columns(s))


def train(X,Y,clf):
	X_train = encode_dataframe(X)
	Y_train = Y
	clf.fit(X_train,Y_train)
	return clf


def predict(X,clf):
	X = encode_dataframe(X)
	return clf.predict(X)
