import numpy as np
import sklearn

X, y = load_data()

svm = sklearn.SVC()
svm.fit(X, y)
predict = svm.predict(X)



