from sklearn.model_selection import GridSearchCV

dt = DecisionTreeClassifier(max_depth=1)
max_samples = 0.05
max_features = 0.5

param_grid = {
	'base_estimator__max_depth': [1, 2, 3, 4, 5],
	'max_samples': [0.05, 0.1, 0.2, 0.5],
	'max_features': [0.5, 0.5, 0.6, 0.7, 0.8, 0.9]
}

def proba(clf, X, y):
	proba = []
	for i, x in enumerate(X):
		p = clf.predict_proba(x)
		proba.append(p[:, 1])
	return np.mean(proba)

def fit_and_predict(X, y):
	bc = BaggingClassifier(dt, n_estimators=20, max_samples=0.5, max_features=0.5)
	bc = bc.fit(X, y)
	return bc.predict(X)


def __starting_point():
	X, y = load_data()
	print(proba(dt, X, y))
	params = param_grid.copy()
	grid = GridSearchCV(dt, params, n_jobs=-1)
	grid.fit(X, y)
	print(grid.best_params_)

__starting_point()
