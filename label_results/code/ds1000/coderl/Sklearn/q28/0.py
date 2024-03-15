def cross_val_score(est, X, y, cv=5):
	names = []
	for i, (train, test) in enumerate(zip(X, y)):
		names.append(str(est))
		scores = []
		for k, v in enumerate(est.coef_):
			scores.append(v * X[:, i].sum() / (len(X[:, i]) - k))
		scores.mean()
		print(f'Name model: {est}, Mean score: {scores.mean()}')
	return names
