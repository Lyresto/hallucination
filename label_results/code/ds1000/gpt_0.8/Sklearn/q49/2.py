One way to handle categorical variables in GradientBoostingClassifier without one-hot encoding is by using the OrdinalEncoder from the scikit-learn library. The OrdinalEncoder can convert categorical variables into integers.

Here's an example of how you can use the OrdinalEncoder to preprocess your categorical variable and merge it back with the original training data:

```python
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import OrdinalEncoder

# Load iris dataset
iris = datasets.load_iris()
X = iris.data[(iris.target == 0) | (iris.target == 1)]
y = iris.target[(iris.target == 0) | (iris.target == 1)]

# Divide data into 80% training, 20% testing.
train_indices = list(range(40)) + list(range(50, 90))
test_indices = list(range(40, 50)) + list(range(90, 100))
X_train = X[train_indices]
X_test = X[test_indices]
y_train = y[train_indices]
y_test = y[test_indices]

# Create a DataFrame from X_train
X_train_df = pd.DataFrame(X_train)

# Insert fake categorical variable
X_train_df['categorical_var'] = ['a'] * 40 + ['b'] * 40

# Initialize OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
# Fit and transform the categorical variable
X_train_encoded = ordinal_encoder.fit_transform(X_train_df[['categorical_var']])

# Convert the encoded variable back into a DataFrame
X_train_encoded_df = pd.DataFrame(X_train_encoded, columns=['categorical_var'])
# Merge the encoded variable with the original training data
X_train_final = pd.concat([X_train_df.drop(columns=['categorical_var']), X_train_encoded_df], axis=1)

# Create and train GradientBoostingClassifier
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train_final, y_train)
```

In this example, the `categorical_var` column is encoded using the OrdinalEncoder and then merged back with the original training data. The resulting `X_train_final` DataFrame contains both the original features and the encoded categorical variable, which can be used to train the GradientBoostingClassifier.

Note: It's important to ensure that the categorical variable is encoded consistently across training and testing datasets. You can use the `ordinal_encoder.transform()` method to encode the categorical variable in the testing dataset as well.