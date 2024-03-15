def split_columns(df):
	print(len(df.columns))
	for i, row in df.iterrows():
		print(i, row)
		if len(row) > 1:
			print('this is a list')
			print(i, row)
			print(len(row))
			for j, col in enumerate(row):
				print(j, col)
				if col:
					df.loc[i, col] = float(col) / len(row)
	print(df.code.values)
	return df
