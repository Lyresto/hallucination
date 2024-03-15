import re

def replace_columns(df):
	return df.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
