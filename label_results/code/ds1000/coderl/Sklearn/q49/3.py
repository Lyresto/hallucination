import numpy as np
import pandas
import sklearn.ensemble

# Create training data
def train(X_train, y_train):
	# Set up encoder
	encoder = sklearn.ensemble.MultiLabelEncoder()
	# Convert training data to matrix
	X_train = encoder.fit_transform(X_train)
	# Split training data into test data
	X_test = encoder.transform(X_test)
	# Build classifier
	clf = GradientBoostingClassifier(max_depth=8, n_estimators=50)
	# Fit and predict on test data
	clf.fit(X_train, y_train)
	# Evaluate trained model
	preds = clf.predict(X_test)
	return preds

def load_data():
	# Get test data
	test = pandas.DataFrame(pd.read_csv("test.csv"))
	# Get train data
	train = pandas.DataFrame(pd.read_csv("train.csv"))
	# Create encoder
	encoder = sklearn.ensemble.MultiLabelEncoder()
	# Convert test data to matrix
	test["PassengerId"] = test["PassengerId"].map(lambda x: int(x) * 40)
	# Convert train data to matrix
	train["PassengerId"] = train["PassengerId"].map(lambda x: int(x) * 40)
	return train, test
