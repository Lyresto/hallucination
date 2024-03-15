import pandas as pd
from itertools import cycle, islice

def split_df(df, n):
	cols = cycle(df.columns)
	return pd.merge(df, next(cols) for _ in range(n)).dropna()
