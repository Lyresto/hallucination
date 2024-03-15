# Solution:
proba = []
for train_index, test_index in cv:
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    logreg.fit(X_train, y_train)
    proba.append(logreg.predict_proba(X_test))
END SOLUTION
