import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.decomposition import PCA
estimators = [('reduce_dim', PCA()), ('poly', PolynomialFeatures()), ('svm', SVC())]

def named_steps(clf):
	if'svm' in clf.steps:
		return list(clf.steps.items())
	elif 'poly' in clf.steps:
		return list(clf.steps.values())
	else:
		return []
