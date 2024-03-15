def df_from_series(s):
	series = list(s.sort_values(by=lambda x: x.split('t'))[:-5:-1])
	index = list(s.index.values[:-5:-1])
	return pd.DataFrame(series, index=index)
