def load_data():
	corpus = pd.read_csv('corpus.csv')
	y = pd.read_csv('y.csv')
	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(corpus)
	selected_feature_names = vectorizer.get_feature_names()
	return X, y, selected_feature_names
