import re

def replace_cols(df):
	for i in df.columns:
		df[i] = re.sub(r'[A-Za-z]', r"&\1<''>", df[i])
	return df
