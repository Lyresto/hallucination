import pandas as pd
import numpy as np
import torch
px = pd.DataFrame(np.random.rand(6,6))

def get_data():
	for i in range(6):
		px[str(i)] = [x.item() if i == 0 else x[i-1] for x in px]
	return px
