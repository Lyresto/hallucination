featureSelector = LinearSVC(penalty='l1', dual=False)
featureSelector.fit(X, y)
selected_feature_names = np.asarray(vectorizer.get_feature_names())[featureSelector.coef_[0] != 0]
