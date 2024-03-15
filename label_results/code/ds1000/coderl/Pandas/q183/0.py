from pandas import Series

def f(d, df):
	s = Series(df['Member'], name='Member')
	for i, v in enumerate(d.values()):
		s[i] = v
	return df.apply(s.fillna, axis=1)
