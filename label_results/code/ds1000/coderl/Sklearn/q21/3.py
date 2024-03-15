import xgboost.sklearn as xgb
from xgboost.model_selection import TimeSeriesSplit
from numpy import sum


def score(b, c, dp):
	return sum(dp[i][j] for i, j in b) / sum(dp[i][j] for i, j in c)


def cross_validate(trainX, trainY, testX, testY, gridsearch):
	cv = TimeSeriesSplit(n_splits=len(trainX)).get_n_splits([trainX, trainY])
	n_jobs = len(cv)
	for i, b in enumerate(gridsearch.grid_scores_):
		testX_tmp = cv.transform([testX[i], testY[i]])
		testY_tmp = cv.transform([testY[i], testY[i]])
		gridsearch.grid_scores_.append((score(b, c, testX_tmp), i))
		gridsearch.best_params_ = b
	return gridsearch


def load_data():
	trainX, trainY = np.array(trainX), np.array(trainY)
	testX, testY = np.array(testX), np.array(testY)
	gridsearch = xgb.XGBRegressor()
	gridsearch.fit(trainX, trainY)
	return gridsearch, testX, testY, trainX, trainY
