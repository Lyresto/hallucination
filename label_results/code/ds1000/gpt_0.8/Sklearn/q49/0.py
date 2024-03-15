One way to handle categorical variables in the GradientBoostingClassifier is to use one-hot encoding. This can be done using the `get_dummies` function from the pandas library.

Here is an example of how you can convert the categorical variable to a matrix and merge it back with the original training data:

```python
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier

# load data in the example
iris = datasets.load_iris()
X = iris.data[(iris.target==0) | (iris.target==1)]
y = iris.target[(iris.target==0) | (iris.target==1)]

# Class 0 has indices 0-49. Class 1 has indices 50-99.
# Divide data into 80% training, 20% testing.
train_indices = list(range(40)) + list(range(50,90))
test_indices = list(range(40,50)) + list(range(90,100))
X_train = X[train_indices]
X_test = X[test_indices]
y_train = y[train_indices]
y_test = y[test_indices]

# Convert X_train to a pandas DataFrame
X_train = pd.DataFrame(X_train)

# Insert fake categorical variable
X_train['category'] = ['a']*40 + ['b']*40

# One-hot encode the categorical variable
X_train_encoded = pd.get_dummies(X_train, columns=['category'])

# Model
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train_encoded, y_train)
```

In this example, the `category` column is one-hot encoded using `pd.get_dummies`, which creates separate columns for each unique value in the `category` column. The encoded features are then used to train the GradientBoostingClassifier.

Note that you will also need to perform the same one-hot encoding on the test data before making predictions.