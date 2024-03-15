from pandas import Series
def solve(df):
	s = series(df['A'])
	for c,i in df.items():
		if 'exp_' in c:
			s[c] = Series(i, name='exp_'+c)
		else:
			s[c] = i**(1,1)
	return s
