def grid_search(clf, X_train, y_train, param_grid):
	print(param_grid)
	cs = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)]
	for i in cs:
		grid = param_grid.copy()
		for k, v in zip(i[0], i[1]):
			grid['base_estimator__{}'.format(k)] = v
			grid['max_samples__{}'.format(k)] = v / sum(v ** i[2])
		print(grid)
		res = bc.fit(X_train, y_train).predict(X_test)
		print(res)
		print(res.argmax(axis=1))
	return bc

def load_data():
	X = pd.read_csv('../data/train.csv')
	y = pd.read_csv('../data/train.csv')
	return X, y
