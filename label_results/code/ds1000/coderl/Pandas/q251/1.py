import pandas as pd

def split_df(df):
	result = []
	for col in df.columns:
		if not all(len(d) == len(df[col]) for d in df.values()):
			result.append(pd.Series(df[col]))
		else:
			split_df_col = pd.Series(df[col])
			split_df_col.fillna(value=np.nan, inplace=True)
			result.append(split_df_col)
	return pd.concat(result)
