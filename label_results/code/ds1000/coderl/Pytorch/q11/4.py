import pandas as pd
import torch

def load_data():
	a, b = torch.from_numpy(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}).values)
	return b[:, a], a[a]
