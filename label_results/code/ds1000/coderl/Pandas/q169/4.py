def remove_zeros(df):
	for i in range(len(df.index)):
		if sum(df.loc[i,col])==0:
			df.loc[i,col] = None
	for j in range(len(df.columns)):
		if sum(df.iloc[:,j])==0:
			df.columns[j] = None
	return df
