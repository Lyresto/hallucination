from operator import xor
from functools import reduce

def df_filtered_series_concat(df, filt):
	df = df.copy()
	for k,v in filt.items():
		df[k] = reduce(xor, df.index.get_level_values(k), 0)
	return df
