from operator import mul
from functools import reduce

def multiply_scores(df, products):
	return df.multiply(lambda row: reduce(mul, (row[k] for k in products), 1.0))
