import pandas as pd

def split_column(df, col):
	sep =''
	strs = [sep.join(df[col].values) for i in range(len(df[col]))]
	return pd.DataFrame(strs)
