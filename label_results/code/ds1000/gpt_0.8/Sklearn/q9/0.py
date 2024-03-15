from sklearn.calibration import CalibratedClassifierCV

# Create the calibrated classifier
calibrated_clf = CalibratedClassifierCV(svmmodel, cv=5)

# Fit the calibrated classifier on the training data
calibrated_clf.fit(X, y)

# Get the probability estimates for the test data
proba = calibrated_clf.predict_proba(x_test)
