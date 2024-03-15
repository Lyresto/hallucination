import numpy as np
import pandas
import sys

def __starting_point():
	X_train, y_train = load_data()
	X_train = pandas.DataFrame(X_train)
	clf = GradientBoostingClassifier(learning_rate=0.01,max_depth=8,n_estimators=50)
	clf.fit(X_train, y_train)

__starting_point()
