from sklearn.ensemble import IsolationForest
from sklearn.externals import joblib

# Load the clean data
clean_data = pd.read_csv("clean_data.csv")

# Fit the model to the clean data
model = IsolationForest()
model.fit(clean_data)

# Save the model
joblib.dump(model, "sklearn_model.pkl")