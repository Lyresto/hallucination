from math import ceil
def sample(df, n, r):
	df2 = df.sample(n, random_state=r)
	return df2.apply(lambda row: int(row['ProductId']) if row['UserId'] in row else 0)
