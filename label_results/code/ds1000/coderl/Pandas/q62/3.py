from collections import OrderedDict

def replace_each_a(df):
	# your code
	dct = OrderedDict()
	for i, x in enumerate(df['a']):
		dct[x] = i+1
	return df.to_dict(dct)
