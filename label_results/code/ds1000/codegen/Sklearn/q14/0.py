
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import PolynomialFeatures
estimators = [('reduce_dim', PCA()), ('poly', PolynomialFeatures()), ('svm', SVC())]
clf = Pipeline(estimators)
clf
