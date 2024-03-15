from pandas import replace

def f(df=example_df):
	for i, j in df.iterrows():
		df.columns[i] = replace("&", "&", str(j))
	return df
