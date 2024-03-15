import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.decomposition import PCA
estimators = [('reduce_dim', PCA()), ('poly', PolynomialFeatures()), ('svm', SVC())]
clf = Pipeline(estimators)
