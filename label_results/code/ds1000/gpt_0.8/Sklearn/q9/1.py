from sklearn.calibration import CalibratedClassifierCV

# Create a CalibratedClassifierCV object
calibrated_model = CalibratedClassifierCV(svmmodel, cv=5)

# Fit the calibrated model
calibrated_model.fit(X, y)

# Obtain probability estimates for the test data
proba = calibrated_model.predict_proba(x_test)
