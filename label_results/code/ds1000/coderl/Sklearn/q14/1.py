from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd

estimators = [('reduce_dim', PCA()), ('svm', SVC())]
clf = Pipeline(estimators)
print(clf.steps)
