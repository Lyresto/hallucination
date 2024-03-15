import pandas as pd
import numpy as np
import sklearn.svm as suppmach


def solve(X, y, x_test):
	svm = suppmach.LinearSVC(penalty='l1', C=1)
	svm.fit(X, y)
	proba = svm.predict(x_test)
	proba_test = svm.decision_function(x_test)
	return (1 / (1 + np.exp(-proba_test)))
