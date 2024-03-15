import xgboost as xgb
from sklearn.model_selection import cross_val_predict


def score(model, x, y):
	return model.score(x, y)


def grid_search(gs, trainX, trainY, testX, testY):
	param_grid = dict(list(zip(trainX, trainY)))
	gs.fit(trainX, trainY, **param_grid)
	b = [score(gs, x, y) for x, y in zip(testX, testY)]
	c = [cross_val_predict(gs, x, y) for x, y in zip(testX, testY)]
	return b, c


def load_data():
	b, c = grid_search(xgb.XGBRegressor(), trainX, trainY, testX, testY)
	return b, c
