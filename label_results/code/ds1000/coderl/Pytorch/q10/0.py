import pandas as pd
import torch

def load_data():
	a, b = pd.read_csv('../../data/input.csv')['A'].values, pd.read_csv('../../data/input.csv')['B'].values
	a = a.astype(np.int64)
	b = b.astype(np.int64)
	return a[b == 1], b
