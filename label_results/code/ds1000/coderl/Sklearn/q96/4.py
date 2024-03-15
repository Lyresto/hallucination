# https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/minmax_scaler.py

from sklearn.preprocessing import MinMaxScaler

def load_data():
	return np.array([[float(i) for i in x] for x in zip(*load_data().T)])
