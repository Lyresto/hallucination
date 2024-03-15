# Use pandas get_dummies to one hot encode the categorical variable
cat_var = pd.get_dummies(X_train[0], prefix='cat')
X_train = pd.concat([X_train.drop(0, axis=1), cat_var], axis=1)

# Model
clf = GradientBoostingClassifier(learning_rate=0.01, max_depth=8, n_estimators=50).fit(X_train, y_train)
