import pandas as pd
def df_filtered(df, filt):
	df2 = df.copy()
	for i, v in enumerate(df.index.get_level_values()):
		df2.iloc[i] = df2.iloc[i].apply(lambda x: x!= v)
	filt2 = filt.copy()
	for i, v in enumerate(filt.index.get_level_values()):
		filt2.iloc[i] = filt2.iloc[i].apply(lambda x: x < v)
	return df2[filt2]
