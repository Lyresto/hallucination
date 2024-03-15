def equalp(x, y):
	return (x == y) or (math.isnan(x) == math.isnan(y) and len(set(x.columns)) == len(set(y.columns)))
