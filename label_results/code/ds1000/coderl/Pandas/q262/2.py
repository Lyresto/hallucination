import pandas as pd

def filter_df(df, filt):
	result = df.copy()
	for k, v in df.index.items():
		if k in filt.index.keys():
			result[k] = df[v]
	return result
