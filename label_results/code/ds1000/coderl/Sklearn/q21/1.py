from xgboost.sklearn import xgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import TimeWindow


def load_data():
	x_train, y_train, x_test, y_test = (pd.read_csv(s) for s in ("train.csv", "test.csv"))
	cv = TimeWindow(n_splits=3)
	param_grid = [{'max_depth': [1, 2, 3],
				  'learning_rate': [0.1, 0.15, 0.2, 0.25, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1, 0.0]}]
	grid = GridSearchCV(xgb.XGBRegressor(), param_grid, n_jobs=1, cv=cv)
	grid.fit(x_train, y_train)
	b = grid.best_score_
	c = grid.best_estimator_.predict(x_test)
	return grid, b, c
