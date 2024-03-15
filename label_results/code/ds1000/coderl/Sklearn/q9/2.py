import numpy as np
import pandas as pd
import sklearn.svm as suppmach

def load_data():
	X = np.array(list(zip(*pd.read_csv('data/input.csv', parse_dates=['Time', 'Value']))))
	y = np.array(list(zip(*pd.read_csv('data/input.csv', parse_dates=['Time', 'Value']))['Value']))
	x_test = np.array(list(zip(*pd.read_csv('data/input.csv', parse_dates=['Time', 'Value']))['Time']))
	
	svmmodel = suppmach.LinearSVC(penalty='l1',C=1)
	svmmodel.fit(X,y)
	proba = svmmodel.predict(x_test)
	return proba
