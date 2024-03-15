def dfo(df):
	d_df = df.copy()
	for i in range(len(df)):
		d_df.loc[df[i] == df[i - 1]] = str(i)
	return d_df

d_df = dfo(pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2']))
