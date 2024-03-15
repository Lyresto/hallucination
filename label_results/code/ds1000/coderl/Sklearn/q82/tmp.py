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




def select_features(X, y, vectorizer, selected_feature_names):
    n_samples = len(X)
    n_features = len(vectorizer.get_feature_names())
    subset = vectorizer.transform(X).nonzero()[0]
    support_mask = np.zeros(n_samples, dtype=bool)
    for i, subset in enumerate(subset):
        if i in selected_feature_names:
            continue
        support_mask[subset] = True
    return support_mask



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(selected_feature_names, f)
