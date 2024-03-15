def predict(X, y):
	X_mean = np.mean(X, axis=0)
	X_std = np.std(X, axis=0)
	return (X - X_mean) / X_std
