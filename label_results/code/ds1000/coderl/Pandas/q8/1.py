from collections import OrderedDict

def drop_if_dup(df, keep='first'):
	res = []
	for col, row in df.iterrows():
		if keep == 'first' and col in OrderedDict:
			res.append([row[0], row[1]])
		elif keep == 'last' and col not in OrderedDict:
			res.append([row[0], row[1]])
		else:
			res.append([row[0], row[1]])
	return pd.DataFrame.from_records(res).drop_duplicates(subset=col, keep=keep)
