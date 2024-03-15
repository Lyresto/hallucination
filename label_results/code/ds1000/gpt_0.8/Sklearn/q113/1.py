from sklearn.ensemble import IsolationForest
import joblib

# Train the model on clean data
X_train = ...

# Fit the model
model = IsolationForest()
model.fit(X_train)

# Save the model to a file
joblib.dump(model, "sklearn_model")