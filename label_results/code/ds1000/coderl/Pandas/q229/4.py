import pandas as pd

def groupby_views(df, bins):
	groups = df.groupby(pd.cut(df.views, bins))
	agg_sum = groups.username.sum()
	return pd.Series(agg_sum, index=df.username)
