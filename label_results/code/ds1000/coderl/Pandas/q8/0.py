from collections import OrderedDict

def drop_duplicates(df, drop_if_dup=None):
	d = OrderedDict()
	for i, j in df.iterrows():
		d[j['url']] = i
		if drop_if_dup is not None and i == d[drop_if_dup]:
			return None
	return df.replace(d, None)
