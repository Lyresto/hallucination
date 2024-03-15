from sklearn.calibration import CalibratedClassifierCV

# Fit model:
svmmodel=suppmach.LinearSVC()

# Create calibrated classifier
calibrated_clf = CalibratedClassifierCV(svmmodel, cv=5, method='sigmoid')

# Fit calibrated classifier
calibrated_clf.fit(X, y)

# Get probability estimates
proba = calibrated_clf.predict_proba(x_test)
