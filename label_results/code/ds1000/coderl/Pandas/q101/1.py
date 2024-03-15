import pandas as pd
def replace_cols(df):
	for col in df:
		if '&' in df[col]:
			df[col] = df[col].replace("&lt;", "<")
	return df
