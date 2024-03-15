from pandas import DataFrame
def fillna(df, dict):
	for c in df:
		df[c] = df[c].astype(str).apply(lambda x: dict.get(x, x))
	return df
