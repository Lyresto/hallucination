One possible solution to convert the features to a 2D-array using sklearn or numpy is by using the OneHotEncoder class from the sklearn.preprocessing module.

Here is an example implementation:

```python
from sklearn.preprocessing import OneHotEncoder

# Initialize the OneHotEncoder object
encoder = OneHotEncoder(sparse=False)

# Fit and transform the features using the encoder
new_features = encoder.fit_transform(features)

# Convert the new_features array to a pandas DataFrame for better visualization
new_features_df = pd.DataFrame(new_features)

# Print the new_features DataFrame
print(new_features_df)
```

This code will convert the features list into a 2D-array where each column corresponds to a unique feature and each row corresponds to a sample. The values in the array represent whether a feature is present or not in a particular sample, with 1 indicating the presence of the feature and 0 indicating the absence.

Note: Make sure to import the necessary modules (pandas, numpy, sklearn) and load the data into the `features` variable before running this code.