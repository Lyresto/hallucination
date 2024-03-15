from sklearn.tree import DecisionTreeClassifier
from randomized_ls import RandomizedLSS

X_train, y_train = load_data()
dt = DecisionTreeClassifier(max_depth=1)
bc = BaggingClassifier(dt, n_estimators=20, max_samples=0.5, max_features=0.5)
param_grid = {
	'base_estimator__max_depth': [1, 2, 3, 4, 5],
	'max_samples': [0.05, 0.1, 0.2, 0.5]
}

#grid search for both decision tree and randomized LSS
param_grid = {
	'base_estimator__max_depth': [1, 2, 3, 4, 5],
	'max_samples': [0.05, 0.1, 0.2, 0.5],
	'randomized_ls': [RandomizedLSS(n_iter=10, random_state=0), RandomizedLSS(n_iter=20, random_state=1)]
}

bc = bc.fit(X_train, y_train)
print(param_grid)
print(bc.best_params_)
