from operator import mul
from functools import reduce


def multiply_scores(df, products):
	multiply = reduce(mul, (float(i[1]) for i in df.groupby('product')))
	return df.apply(mul, {'score': multiply})
