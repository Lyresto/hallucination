One way to convert categorical variables to matrix using `get_dummies` in pandas is as follows:

```python
X_train_categorical = pd.get_dummies(X_train[0], prefix='var')
X_train_encoded = pd.concat([X_train, X_train_categorical], axis=1)
X_train_encoded = X_train_encoded.drop([0], axis=1)
```

This will create dummy variables for the categorical variable `X_train[0]`, with prefix 'var'. The encoded categorical variables are then concatenated with the original training data, and the original categorical variable is dropped.

After encoding the categorical variable, you can use the encoded data to train your model:

```python
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train_encoded, y_train)
```

Note that if you have multiple categorical variables, you can repeat the above steps for each categorical variable and then concatenate all the encoded categorical variables with the original training data.