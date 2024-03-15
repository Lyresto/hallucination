from sklearn.calibration import CalibratedClassifierCV

# Create the CalibratedClassifierCV object with the LinearSVC model
calibrated_model = CalibratedClassifierCV(model, cv=5)

# Fit the model on the training data
calibrated_model.fit(X, y)

# Use the calibrated model to predict probabilities
proba = calibrated_model.predict_proba(x_predict)
