from itertools import chain

def value(col):
	try:
		return df[col].min()
	except:
		return 1

def filter_rows(df,n):
	return (df[c for c in range(n) if abs(value(df[c])) <= 1]
			.filter(lambda x: len(list(x.values())) > n))
