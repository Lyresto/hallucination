from sklearn.calibration import CalibratedClassifierCV

# Create a calibrated classifier
calibrated_clf = CalibratedClassifierCV(svmmodel, cv=5)

# Fit the calibrated classifier
calibrated_clf.fit(X, y)

# Get the predicted probabilities
proba = calibrated_clf.predict_proba(x_test)
