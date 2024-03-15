import pandas as pd
from itertools import zip_longest

def melt(df, value_vars, var_name=''):
	print(df)
	print(value_vars)
	print(var_name)
	result = [list(v) for v in zip_longest(*zip(*value_vars))]
	print(result)
	for i, v in enumerate(result):
		df.columns[i] = v
	print(df.columns)
	return df
