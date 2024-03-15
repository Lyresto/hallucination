One way to handle categorical variables in GradientBoostingClassifier without one hot encoding is by using the pandas `get_dummies` function. Here's how you can do it:

```python
# Load data
iris = datasets.load_iris()
X = iris.data[(iris.target==0) | (iris.target==1)]
Y = iris.target[(iris.target==0) | (iris.target==1)]

# Divide data into 80% training, 20% testing.
train_indices = list(range(40)) + list(range(50,90))
test_indices = list(range(40,50)) + list(range(90,100))
X_train = X[train_indices]
X_test = X[test_indices]
y_train = Y[train_indices]
y_test = Y[test_indices]

# Create a DataFrame from X_train
X_train_df = pd.DataFrame(X_train)

# Create a categorical variable column
X_train_df['categorical_var'] = ['a']*40 + ['b']*40

# Use get_dummies to convert categorical_var into a matrix
categorical_var_dummies = pd.get_dummies(X_train_df['categorical_var'], prefix='categorical_var')

# Merge the dummies matrix with the original training data
X_train_df = pd.concat([X_train_df, categorical_var_dummies], axis=1)

# Drop the original categorical variable column
X_train_df.drop('categorical_var', axis=1, inplace=True)

# Model
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train_df, y_train)
```

This code creates a new DataFrame `X_train_df` from `X_train`, adds a categorical variable column, uses `get_dummies` to convert the categorical variable into a matrix, merges the dummies matrix with the original training data, and finally drops the original categorical variable column before fitting the model.