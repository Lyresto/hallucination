def replace_each_a(df):
	for i, row in enumerate(df.values):
		if i == 0:
			continue
		df['a'][i] = str(int(row[0]))
	return df
