import pandas as pd

def pd_to_series(df):
	# your code
	ts = pd.Series(df['Value'], index=df['Date'])
	return ts
