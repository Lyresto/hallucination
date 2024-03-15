import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

slopes = []
for col in df1.columns:
	df2 = df1[~np.isnan(df1[col])]
	npMatrix = np.matrix(df2)
	X, Y = npMatrix[:, 0], npMatrix[:, 1]
	slope = LinearRegression().fit(X,Y)
	m = slope.coef_[0]
	slopes.append(m)

df1['Z3'] =lopes[0]

