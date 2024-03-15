from pandas import Series, DataFrame

def solve(df):
	s = Series(df.v, index=df.l)
	return pd.Series(s.sum(skipna=False), index=df.l).sum()
