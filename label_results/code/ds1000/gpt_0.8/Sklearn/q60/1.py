# One way to achieve this is by using the sklearn.feature_extraction.text.CountVectorizer class. 
# This class is typically used for text data, but we can also use it for our purposes.
# First, we need to convert each sample's features into a single string representation.

sample_features = [' '.join(sample) for sample in features]

# Then, we can use CountVectorizer to convert the string representations into a matrix of token counts.

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(binary=True)
new_features = vectorizer.fit_transform(sample_features).toarray()

# The resulting new_features matrix will have binary values indicating the presence or absence of each feature in each sample.

# Finally, we can convert the matrix into a pandas DataFrame for easier visualization.

new_features = pd.DataFrame(new_features, index=['s1', 's2', 's3'], columns=vectorizer.get_feature_names())

new_features
