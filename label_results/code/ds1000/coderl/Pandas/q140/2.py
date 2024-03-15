from pandas import DataFrame

def query_series(df, expr):
	var = expr.split('!')
	try:
		if var[0] == 'True':
			s = eval(expr)
			return df.loc[s.index(True)]
	except:
		return df.loc[0]

def query_df(df, expr):
	var = expr.split('!')
	try:
		if var[0] == 'True':
			return df.query(expr)
	except:
		return df.loc[0]
