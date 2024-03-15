from functools import reduce

def state(df, s):
	return reduce(lambda x, y: x + y, (v for row in df.values() for v in row if v > 50), 0)
