from sklearn.calibration import CalibratedClassifierCV

calibrated_model = CalibratedClassifierCV(base_estimator=model, cv=5, method='sigmoid')
calibrated_model.fit(X, y)

proba = calibrated_model.predict_proba(x_predict)
