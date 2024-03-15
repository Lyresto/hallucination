from pandas import DataFrame
def query(df, expr):
	try:
		l = list(expr.split('!'))
	except:
		return df
	i = 0
	while i < len(l):
		if eval(l[i]):
			return df.ix[i::,df.columns.get("Category")!= "Foo"]
		i += 1
