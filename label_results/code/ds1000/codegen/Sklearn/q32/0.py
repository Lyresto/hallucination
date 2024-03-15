
clf = GridSearchCV(bc, param_grid, cv=5, verbose=2, n_jobs=-1)
clf.fit(X_train, y_train)
proba = clf.predict_proba(X_test)
