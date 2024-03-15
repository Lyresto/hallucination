import pandas as pd

def split_dataframe_to_multiple_rows(df):
	strings = [df[col].str.split(sep=' ') for col in df.columns]
	result = pd.DataFrame(strings, index=[0]*len(df.columns), columns=df.columns)
	return result.compute()
