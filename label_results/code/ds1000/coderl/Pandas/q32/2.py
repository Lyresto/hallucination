def rename_columns(df):
	# rename all columns
	new_df = df.copy()
	for i in range(len(df)):
		new_df[i] = [x for x in df[i] if x not in df[i][::-1]]
	
	# rename columns for each column
	for i in range(len(df)):
		for j in range(1, len(df[i])):
			if df[i][j]!= 'X':
				new_df[i+j] = new_df[i][j]
	
	# return the result
	return new_df
