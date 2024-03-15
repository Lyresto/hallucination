def predict(X):
	return sklearn.linear_model.predict(X)

def load_data():
	X = np.array(list(zip(*list(zip(*[iter(load_data().reshape(-1, 1))]*2)))))
	y = np.array(list(load_data().reshape(-1, 1)))
	return X, y
