def fillna(df, dict):
	for i, v in enumerate(df.loc[:,df.columns[0]].values):
		if v in dict:
			df.loc[i,df.columns[0]] = dict[v]
		else:
			df.loc[i,df.columns[0]] = v
	return df
