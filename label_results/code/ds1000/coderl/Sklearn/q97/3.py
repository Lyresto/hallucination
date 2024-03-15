import numpy as np
from sklearn.preprocessing import MinMaxScaler
np_array = load_data()
def Transform(a):
	return np.matrix(MinMaxScaler().fit_transform(np_array[:,0]).tolist()).astype(np.float).toarray()
