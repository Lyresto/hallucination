featureSelector = LinearSVC(penalty='l1', dual=False)
featureSelector.fit(X, y)
selected_feature_indices = np.where(featureSelector.coef_ != 0)[1]
selected_feature_names = np.asarray(vectorizer.get_feature_names())[selected_feature_indices]
