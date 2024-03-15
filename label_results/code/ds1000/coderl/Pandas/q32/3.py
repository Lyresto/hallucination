def rename_columns(df):
	"""
	Rename All Columns
	"""
	s = ''
	for c in df.columns:
		if c[-1] == 'X':
			s += c + 'X'
		else:
			s += c
	df.columns = [x.rstrip('X') for x in df.columns]
	return df
