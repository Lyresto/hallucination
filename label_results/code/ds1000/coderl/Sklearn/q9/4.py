from sklearn.svm import LinearSVC

def proba(x_test):
	svm = LinearSVC(penalty='l1', C=1)
	svm.fit(x_test, y)
	return 1 / (1 + np.exp(-svm.predict(x_test)))

def load_data():
	X = np.array([[i, j] for i, j in zip(X, y)])
	y = np.array([j for i, j in zip(X, y)])
	x_test = np.array([i for i, j in zip(x_test, y)])
	return X, y, x_test
