def df_with_id(df):
	return df.map(lambda row: str(row['a']) + row['b'] + row['c'], df.index.names)
