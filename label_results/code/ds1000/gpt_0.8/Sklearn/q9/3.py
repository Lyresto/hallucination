from sklearn.calibration import CalibratedClassifierCV

# Create a calibrated classifier using LinearSVC as the base estimator
calibrated_svc = CalibratedClassifierCV(svmmodel, cv=5)

# Fit the calibrated classifier on the training data
calibrated_svc.fit(X, y)

# Predict probabilities for the test data
proba = calibrated_svc.predict_proba(x_test)
