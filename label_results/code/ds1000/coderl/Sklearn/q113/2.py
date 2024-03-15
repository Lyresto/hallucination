from sklearn.ensemble import IsolationForest

def load_data():
	return pd.read_csv("sklearn_model.csv")

def predict(X):
	return IsolationForest().fit(X).predict(X)
