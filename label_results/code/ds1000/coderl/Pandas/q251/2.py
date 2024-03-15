def split_columns(df):
	codes = df['codes']
	for i, col in enumerate(codes):
		if len(col) > 1:
			df[col] = df[col].apply(lambda x: float(x.pop(0)), axis = 1)
	return df
