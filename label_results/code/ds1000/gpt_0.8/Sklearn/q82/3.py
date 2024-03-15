selected_feature_names = np.asarray(vectorizer.get_feature_names())[np.abs(svc.coef_).argmax(axis=0)]
