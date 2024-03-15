from functools import reduce
def f(df=example_df):
	return reduce(lambda a, b: a.replace("&", "&"), df.columns)
