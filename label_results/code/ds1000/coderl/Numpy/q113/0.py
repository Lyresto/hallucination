def df_init(df):
	for a,b in zip(df.columns,df.values):
		if type(a) is not int:
			df[a]=df[a].astype(float)
		if type(b) is not float:
			df[b]=df[b].astype(float)
	return df
