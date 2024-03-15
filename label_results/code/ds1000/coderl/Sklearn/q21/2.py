from xgboost import xgb
from sklearn.model_selection import GridSearchCV

def search(x, y, param_grid, n_splits=3):
	param_grid["eval_set"] = [[x, y]]
	grid = GridSearchCV(xgb.XGBRegressor(), param_grid, n_splits=n_splits, verbose=1)
	grid.fit(x, y)
	print(grid.best_params_)
	return grid.best_params_["eval_metric"]

def predict(x, y, param_grid):
	return search(x, y, param_grid, 2)

def score(x, y, param_grid):
	return search(x, y, param_grid, 1)[0]

def load_data():
	s = pd.DataFrame({"x": range(len(trainX)), "y": trainY})
	t = pd.DataFrame({"x": range(len(testX)), "y": testY})
	param_grid = { "x__range": [0, 1],
				  "y__in": [0, 1]}
	
	print(search(s, t, param_grid, 3))
	return score(s, t, param_grid), predict(s, t, param_grid), search(s, t, param_grid, 3)
