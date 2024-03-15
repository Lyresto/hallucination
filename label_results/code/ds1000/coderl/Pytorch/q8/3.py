import torch
import numpy as np
import pandas as pd
from collections import OrderedDict

def convert_to_dataframe(px):
	px_t = {}
	for i,row in enumerate(px.values):
		px_t[i] = list(row)
	return pd.DataFrame(px_t)

def load_data():
	x = np.array([[0,1,2,3,4,5],
				[1,2,3,4,5,6],
				[2,3,4,5,6,7],
				[3,4,5,6,7,8],
				[4,5,6,7,8,9],
				[5,6,7,8,9,0]])
	return x
