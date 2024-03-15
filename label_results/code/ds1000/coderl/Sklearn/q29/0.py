from sklearn.decomposition import NMF
from sklearn.feature_extraction import TfidfVectorizer

def transform(data):
	tfidf = TfidfVectorizer()
	nmf = NMF(n_components=2)
	tfidf.fit_transform(data.test)
	tfidf_out = tfidf.components_.tolist()
	
	return pd.DataFrame(tfidf_out, index=data.test)
