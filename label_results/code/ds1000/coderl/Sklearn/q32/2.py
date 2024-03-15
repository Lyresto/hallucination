import numpy as np
import pandas as pd

def find_best(clf, param_grid):
	grid = param_grid.copy()
	for i in range(len(param_grid['max_samples'])):
		grid['max_samples'][i] = np.log(param_grid['max_samples'][i])
	for i in range(len(param_grid['base_estimator__max_depth'])):
		grid['base_estimator__max_depth'][i] = param_grid['base_estimator__max_depth'][i]
	
	# A = np.array(param_grid['max_samples'])
	# B = np.array(param_grid['base_estimator__max_depth'])
	# C = np.array(param_grid['max_features'])
	
	grid_search = GridSearchCV(clf, **grid)
	grid_search.fit(X_train, y_train)
	return grid_search.best_params_

