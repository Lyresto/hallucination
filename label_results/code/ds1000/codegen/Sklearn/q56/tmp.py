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
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
queries, documents = load_data()
assert type(queries) == list
assert type(documents) == list
tfidf = TfidfVectorizer()
tfidf.fit_transform(documents)
cosine_similarities_of_queries =... # put solution in this variable
END SOLUTION

"""

"""
<|python|>#
### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cosine_similarities_of_queries, f)
