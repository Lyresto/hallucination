def df_filter(df, n):
	new_df = df.copy()
	for i in range(n):
		for j in range(len(df.columns)):
			if abs(df[j][i])<1:
				new_df[j]=new_df[j][:i]+'Value'+new_df[j][i+1:]
	return new_df
