import numpy as np
import pandas as pd

def load_data():
	np_array = np.array(pd.read_csv('data.csv'))
	scaler = MinMaxScaler()
	return scaler.fit_transform(np_array[:, 1:])
