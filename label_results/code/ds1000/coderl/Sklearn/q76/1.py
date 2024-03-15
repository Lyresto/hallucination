def split_data():
	X = dataset.values[:-1]
	Y = dataset.values[-1]
	X_train, X_test = [], []
	y_train, y_test = [], []
	for i in range(len(X)):
		if i % 2 == 0:
			y_train.append(Y[i])
		else:
			y_test.append(Y[i])
	return (X_train, X_test, y_train, y_test)
