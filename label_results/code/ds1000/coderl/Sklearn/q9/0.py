from sklearn.svm import LinearSVC

def proba(X,y):
	# Predict on test data:
	pred = LinearSVC(penalty='l1', C=1).predict(X)
	# Convert decision function to probabilities:
	proba = 1 / (1 + np.exp(pred - X))
	return proba

def load_data():
	# Data loading:
	X = np.array(list(zip(X,y)))
	y = np.array(list(zip(X,y)))
	X_test = np.array(list(zip(X_test,[1]*len(X_test))))
	return X,y,X_test
