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
from scipy.spatial import cosine_similarity




def get_tf_idf_query_similarity(queries, documents):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)
    return cosine_similarity(matrix, queries).tolist()




def get_term_frequency_inverse_data_frequency(documents):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)
    return matrix.toarray()



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cosine_similarities_of_queries, f)
