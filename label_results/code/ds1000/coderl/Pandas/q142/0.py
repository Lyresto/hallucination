import pandas as pd

def melt(df, value_vars):
	new_cols = list(df.columns)
	for i, v in enumerate(value_vars):
		new_cols[i] = [v[0] for _ in range(len(v))] + v[1:]
	return pd.melt(df, new_cols)
