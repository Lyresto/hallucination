import sklearn.svm as suppmach
import numpy as np
from scipy import stats

def linear_svc_probability(X, y, x_test):
	svm = suppmach.LinearSVC(penalty='l1', C=1)
	predicted = svm.predict(x_test)
	test_prob = svm.decision_function(x_test)
	return stats.probit(predicted) / test_prob





def load_data():
	X = np.array(list(zip(X,y)))
	x_test = np.array(list(zip(X,x_test)))
	return X, y, x_test
