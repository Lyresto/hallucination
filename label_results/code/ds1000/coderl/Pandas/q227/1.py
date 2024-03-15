import pandas as pd
import numpy as np

def create_dataframe_with_cycles(a, b, c):
	f, m = [], len(a) + len(b)
	for i, df in enumerate((a, b, c)):
		for j in range(m):
			f.append(pd.DataFrame(np.array([[j + 1, j + 2] for j in range(len(df))]), columns=['row', 'col']))
	return f[0]
