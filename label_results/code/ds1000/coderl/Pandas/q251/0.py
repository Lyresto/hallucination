def split_dataframe(df):
	codes = df['codes']
	columns = ['code_' + str(i) for i in range(1, len(codes)+1)]
	new_df = pd.DataFrame(columns=columns)
	for i in range(len(codes)):
		values = codes[i]
		new_df['code_' + str(i)] = pd.to_numeric(values)
	new_df.fillna(value=np.nan,inplace=True)
	return new_df
