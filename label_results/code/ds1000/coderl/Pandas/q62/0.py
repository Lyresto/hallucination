def df_to_output(df):
	new_df = pd.DataFrame()
	for i, v in enumerate(df['a']):
		new_df['name'][i] = v
	return new_df
