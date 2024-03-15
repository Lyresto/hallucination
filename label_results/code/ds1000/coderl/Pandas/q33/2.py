import pandas as pd
def mean(df):
	v_col = df.columns.values
	return pd.DataFrame(dict.fromkeys(v_col), index=v_col).mean()
