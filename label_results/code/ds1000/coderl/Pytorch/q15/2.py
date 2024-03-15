import pandas as pd
import numpy as np
import torch

def index_select(idx, B):
	#print(idx, B)
	new_index_columns = list(zip(idx, B))
	#print(new_index_columns)
	new_tensors = []
	for i, j in new_index_columns:
		#print(i, j)
		new_tensors.append([j[i] for i in range(len(j))])
	return torch.LongTensor(new_tensors)
