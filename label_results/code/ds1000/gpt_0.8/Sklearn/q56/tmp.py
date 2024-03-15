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
# Transform the query into a tf-idf vector representation
query_vector = tfidf.transform(queries)

# Calculate the cosine similarity between the query vector and the document vectors
cosine_similarities_of_queries = np.dot(query_vector, tfidf_matrix.T)

# Convert the cosine similarities into a dataframe for easier visualization
cosine_similarities_of_queries = pd.DataFrame(cosine_similarities_of_queries, columns=documents)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cosine_similarities_of_queries, f)
