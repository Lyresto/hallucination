def df_filter(df, n):
	output = []
	for i in range(len(df['A_Name'])):
		if abs(sum(df[x] for x in df.columns) - 1) < 1:
			output.append(df[i])
	return output
