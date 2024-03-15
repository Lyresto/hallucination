import re

def replace_columns(df):
	for i, row in df.iterrows():
		if re.search(r"[A-Za-z\s]{2,}", row):
			df.loc[i, i] = df.loc[i, i].replace("[A-Za-z\s]{2,}", "<")
	return df
