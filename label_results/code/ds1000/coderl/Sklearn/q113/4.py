from collections import defaultdict
from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib

def load_data():
	return joblib.load(filename="sklearn_model")

def predict(fitted_model, X):
	y = fitted_model.predict(X)
	return y
