clf = LinearSVC(penalty='l1', dual=False)
clf.fit(X, y)
coef = clf.coef_
selected_feature_indices = np.where(coef[0]!=0)[0]
selected_feature_names = np.asarray(vectorizer.get_feature_names())[selected_feature_indices]
