from sklearn import datasets, cross_validation
from itertools import chain

def split_data():
	ds = datasets.load_csv('example.csv', header=None, sep=',')
	x = list(chain.from_iterable((d[:-1] for d in ds.split(",")[1:])))
	y = list(chain.from_iterable((d[:-1] for d in ds.split(",")[0:])))
	return x, y

def __starting_point():
	x_train, y_train = split_data()
	x_test, y_test = split_data()
