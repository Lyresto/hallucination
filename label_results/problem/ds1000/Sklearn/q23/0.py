proba = []
for train, test in cv:
    logreg.fit(X[train], y[train])
    proba.append(logreg.predict_proba(X[test]))
proba = np.concatenate(proba)
