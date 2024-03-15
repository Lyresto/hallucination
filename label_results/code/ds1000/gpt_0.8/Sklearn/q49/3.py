One way to handle categorical variables in GradientBoostingClassifier without one-hot encoding is to use the LabelEncoder from the scikit-learn library. The LabelEncoder converts each categorical value into a numerical label. Here's an example of how you can use the LabelEncoder to handle the categorical variable in your code:

```python
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder

iris = datasets.load_iris()
# Use only data for 2 classes.
X = iris.data[(iris.target==0) | (iris.target==1)]
Y = iris.target[(iris.target==0) | (iris.target==1)]

# Class 0 has indices 0-49. Class 1 has indices 50-99.
# Divide data into 80% training, 20% testing.
train_indices = list(range(40)) + list(range(50,90))
test_indices = list(range(40,50)) + list(range(90,100))
X_train = X[train_indices]
X_test = X[test_indices]
y_train = Y[train_indices]
y_test = Y[test_indices]

# Create a LabelEncoder object
le = LabelEncoder()
# Fit and transform the categorical variable in the training data
X_train_encoded = le.fit_transform(X_train[:, 0])
# Merge the encoded variable with the original training data
X_train_encoded = np.column_stack((X_train_encoded, X_train[:, 1:]))

# Model.
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train_encoded, y_train)
```

In this example, we use the `fit_transform` method of the LabelEncoder to transform the first column of `X_train` into numerical labels. We then merge the encoded variable with the rest of the training data using `np.column_stack`.

Note that this approach assumes that the categorical variable has a meaningful ordinal relationship, meaning that the order of the categories matters. If the categories are unordered or have no meaningful order, one-hot encoding would be a more appropriate approach.