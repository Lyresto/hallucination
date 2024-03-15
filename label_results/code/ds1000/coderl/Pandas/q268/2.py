def df_to_ts(df):
	#your code here
	dates = [pd.to_datetime(df[c]) for c in df]
	values = df['Value']
	return pd.Series(values, index=dates)
