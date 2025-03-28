import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

queries, documents = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
tfidf = TfidfVectorizer()
tfidf.fit_transform(documents)
### BEGIN SOLUTION
query_tfidf = tfidf.transform(queries)
cosine_similarities_of_queries = np.dot(query_tfidf, tfidf.T).toarray()

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cosine_similarities_of_queries, f)
