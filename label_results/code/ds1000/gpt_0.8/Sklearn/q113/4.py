from sklearn.ensemble import IsolationForest
import joblib

# Fit the model to your clean data
model = IsolationForest()
model.fit(X_train)

# Save the model to a file
joblib.dump(model, "sklearn_model.pkl")
