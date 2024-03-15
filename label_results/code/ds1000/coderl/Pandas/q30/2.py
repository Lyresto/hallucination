from collections import OrderedDict

def rename_columns(df):
	d = OrderedDict()
	for k, v in df.items():
		d[k] = v
	return df.rename(columns=d)
