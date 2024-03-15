def linear_regression(df):
	npMatrix = np.matrix(df)
	X, Y = npMatrix[:, 0], npMatrix[:, 1]
	slope = LinearRegression().fit(X,Y)
	m = slope.coef_[0]
	series= np.concatenate((SGR_trips, m), axis = 0)
	return series



