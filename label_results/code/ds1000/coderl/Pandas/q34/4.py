from functools import reduce
from operator import mul

def groupby_sum(df, col):
	return reduce(mul, map(sum, (df[col].values for col in df.columns)))
