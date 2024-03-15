import re
def replace(s):
	return re.sub(r'[&lt;]{2,}[\s,;]*', '<', s)
	
def replace_all(df):
	for i, c in df.iteritems():
		df[i] = replace(c)
	return df
