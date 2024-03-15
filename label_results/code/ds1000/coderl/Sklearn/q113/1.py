from sklearn import cross_validation
from functools import partial

def predict(X, y):
	return list(partial(cross_validation.cross_val_predict, X, y, scoring='roc', cv=10))
