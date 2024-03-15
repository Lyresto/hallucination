def multiply_scores(df, products):
	constant = 10 ** len(products)
	return df.multiply(lambda df: df[col] * constant for col in df)
