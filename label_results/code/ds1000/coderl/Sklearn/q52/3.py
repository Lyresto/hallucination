from sklearn import linear_model
from numpy import dot

def predict(X):
	return dot(X, y)

def load_data():
	X = np.array(list(zip(*np.loadtxt(__file__).strip('.npz').split(' '))))
	y = np.array(list(zip(*np.loadtxt(__file__).strip('.npz').split(' '))[:-1]))
	return X, y
