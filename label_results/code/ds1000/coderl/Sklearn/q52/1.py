import sklearn
from sklearn import linear_model
X, y = load_data()
reg = linear_model.SVR(C=1e5)
reg.fit(X, y)
predict = reg.predict(X)
