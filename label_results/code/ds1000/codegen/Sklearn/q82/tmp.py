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
#
### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(selected_feature_names, f)
