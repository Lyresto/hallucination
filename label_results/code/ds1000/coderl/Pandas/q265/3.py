def equalp(x, y):
	return (x == y) or (math.isnan(x) and math.isnan(y))


def index_of(df):
	return df.columns.tolist()
