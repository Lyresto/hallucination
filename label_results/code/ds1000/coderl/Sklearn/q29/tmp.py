import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.pipeline import Pipeline

data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
pipe = Pipeline([
    ("tf_idf", TfidfVectorizer()),
    ("nmf", NMF())
])
### BEGIN SOLUTION
from sklearn.decomposition import NMF
from sklearn.feature_extraction import TfidfVectorizer




def transform(data):
    tfidf = TfidfVectorizer()
    nmf = NMF(n_components=2)
    tfidf.fit_transform(data.test)
    tfidf_out = tfidf.components_.tolist()
    
    return pd.DataFrame(tfidf_out, index=data.test)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(tf_idf_out, f)
