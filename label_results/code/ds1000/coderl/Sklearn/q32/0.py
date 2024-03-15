from sklearn.tree import DecisionTreeClassifier
from scipy.stats import pprob

def proba(X_test, y_test):
	dt = DecisionTreeClassifier(max_depth=1)
	param_grid = {
		'base_estimator__max_depth': [1, 2, 3, 4, 5],
		'max_samples': [0.05, 0.1, 0.2, 0.5],
	}
	ls = []
	for i, (X_i, y_i) in enumerate(zip(X_test, y_test)):
		ls.append(pprob(dt, X_i).mean())
	bc = BaggingClassifier(dt, n_estimators=20, max_samples=0.5, max_features=0.5, **param_grid)
	bc = bc.fit(X_test, y_test)
	return ls + [bc.score(X_test, y_test)]
