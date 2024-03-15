from sklearn.ensemble import IsolationForest
import joblib

# Train the model on clean data
X_train = ...

model = IsolationForest()
model.fit(X_train)

# Save the model
joblib.dump(model, "sklearn_model.joblib")
