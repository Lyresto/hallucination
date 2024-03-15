import numpy as np
import pandas as pd

def select_features(X, y, vectorizer, selected_feature_names):
	n_samples = len(X)
	n_features = len(vectorizer.get_feature_names())
	subset = vectorizer.transform(X).nonzero()[0]
	support_mask = np.zeros(n_samples, dtype=bool)
	for i, subset in enumerate(subset):
		if i in selected_feature_names:
			continue
		support_mask[subset] = True
	return support_mask
