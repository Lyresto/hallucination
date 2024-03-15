def combine_name_and_a(df):
	dct = {}
	for key, val in df.items():
		dct[val] = key
	return pd.DataFrame(dct).replace('ID', str).values.tolist()
