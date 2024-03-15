from sklearn.calibration import CalibratedClassifierCV

# Fit the model with probability calibration
calibrated_model = CalibratedClassifierCV(model, cv=5, method='sigmoid')
calibrated_model.fit(X, y)

# Get probability estimates for the test data
proba = calibrated_model.predict_proba(x_predict)
