import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

corpus, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
### BEGIN SOLUTION
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



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(selected_feature_names, f)
