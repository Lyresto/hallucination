from sklearn.feature_selection import SelectFromModel

# Create the LinearSVC model
model = LinearSVC(penalty='l1', dual=False)

# Fit the model to the data
model.fit(X, y)

# Get the feature indices of the selected features
selected_feature_indices = model.coef_.nonzero()[1]

# Get the names of the selected features
selected_feature_names = np.asarray(vectorizer.get_feature_names())[selected_feature_indices]
