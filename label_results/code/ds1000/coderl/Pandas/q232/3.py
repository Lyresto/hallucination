from pandas import DataFrame

def merge_rows(df):
	df = df.merge(df, left_on="text", right_on="text")
	return df.iloc[0]["text"]
