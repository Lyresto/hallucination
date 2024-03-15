def equalp(x, y):
	return x.equals(y) or (math.isnan(x.values[0]) and math.isnan(y.values[0]))
