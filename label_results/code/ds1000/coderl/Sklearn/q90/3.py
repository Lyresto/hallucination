import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def iterate_over_columns(df1):
	df2 = df1[~np.isnan(df1['A1'])]
	df3 = df2[['Time','A1']]
	npMatrix = np.matrix(df3)
	X, Y = npMatrix[:, 0], npMatrix[:, 1]
	slope = LinearRegression().fit(X,Y)
	m = slope.coef_[0]
	series = np.concatenate((SGR_trips, m), axis = 0)
	return [series[i] for i in range(len(series))]
