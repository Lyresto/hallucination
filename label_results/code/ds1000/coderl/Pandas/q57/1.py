def min_max_expand(df):
	m, f = min(df['dt']), lambda x: (0, 0) if x in df else (x, df['val'][0])
	for i in range(len(df['dt'])):
		m = min(m, pd.to_datetime(df['dt'][i]))
		f = lambda x: (0 if x in df else x, df['val'][x])
	return df.apply(f)
