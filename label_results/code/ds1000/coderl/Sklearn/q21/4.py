from xgboost.sklearn import xgb
from numpy import *

def gridsearch(x, y, train, test, score, param_grid):
	n_splits = len(train)
	cv_params = [{str(k): v for k, v in param_grid.items() if k!= 'n_splits'}]
	n_stop_rounds = int(score['early_stopping_rounds'])
	# print(n_splits, n_stop_rounds)
	best = xgb.XGBRegressor(**param_grid)
	# best.fit(train, y)
	for n_stop in range(n_stop_rounds + 1):
		best.fit(train[n_splits:], y[n_splits:])
		# print(best.best_score_, best.best_params_)
		if best.best_score_ < n_stop * score['eval_metric']:
			best = best.best
			n_stop_rounds = n_stop
		elif best.best_score_ == n_stop * score['eval_metric']:
			# print('best: ', best)
			break
	# print(best)
	test_score = best.predict(test[n_splits:])
	# print('test score: ', test_score, '\n')
	return test_score

def load_data():
	n, m = len(train), len(train[0])
	train = ([[x, y] for x, y in zip(train, train[1:])] for _ in range(n))
	test = ([[x, y] for x, y in zip(test, test[1:])] for _ in range(n))
	param_grid = {
		'n_splits': [1, 2, n, m], 
		'eval_metric' : [mean_error, mean_precision, mean_f1, mean_s1, mean_error]
	}
	return gridsearch(train, test, train, test, score=0, param_grid=param_grid)

mean_error = lambda x: sum(y_