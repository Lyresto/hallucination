import pandas as pd
def time_rank(df):
	return pd.Series(df['TIME'].values, index=df['ID']).rank(ascending=False)
