def df_cum(df, column_name):
	try:
		cumsum = df[column_name]
	except:
		cumsum = np.cumsum(df['Q'])
		df[column_name] = cumsum
	return cumsum
