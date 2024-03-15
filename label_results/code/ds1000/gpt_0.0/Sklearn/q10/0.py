from sklearn.calibration import CalibratedClassifierCV
calibrated_model = CalibratedClassifierCV(model, cv=5)
calibrated_model.fit(X, y)
proba = calibrated_model.predict_proba(x_predict)
