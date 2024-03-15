from pandas import DataFrame
def fillna(df, d):
	for c,v in df.iterrows():
		df[c] = df[c].fillna(d.get(v, None))
	return df
