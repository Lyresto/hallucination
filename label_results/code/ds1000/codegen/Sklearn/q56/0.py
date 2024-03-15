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