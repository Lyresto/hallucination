import numpy as np
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

corpus, y = load_data()
assert type(corpus) == list
assert type(y) == list

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Perform feature selection using LinearSVC with L1 penalty
lsvc = LinearSVC(penalty='l1', dual=False)
lsvc.fit(X, y)

# Retrieve the feature indices of the selected features
selected_feature_indices = np.where(lsvc.coef_ != 0)[1]

# Retrieve the feature names using the vectorizer
selected_feature_names = np.asarray(vectorizer.get_feature_names())[selected_feature_indices]
