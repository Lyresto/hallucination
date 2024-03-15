from sklearn.model_selection import StratifiedKFold

def proba(y, X):
	scores = []
	for train, test in StratifiedKFold(y, n_tests=len(X)).split(X):
		logreg.fit(X[train], y[train])
		prob = logreg.predict_proba(X[test])
		scores.append(prob)
	return scores
