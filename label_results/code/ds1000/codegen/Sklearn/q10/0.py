model = svm.LinearSVC(C=1, penalty='l1')
model.fit(X, y)
proba = model.predict_proba(X)
