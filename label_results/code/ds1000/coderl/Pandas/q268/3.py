def df_to_series(df):
	ts = df.copy()
	for i, d in enumerate(df.index):
		ts.loc[d,'Date'] = pd.to_datetime(ts.loc[d,'Date'])
	return ts
