def sample_df(df):
	result = df.copy()
	for _ in range(int(len(df) * 0.8)):
		quantity = 0
		for index, item in enumerate(df['UserId']):
			if item == result.index[0]:
				quantity += 1
		df['Quantity'] = [0] * len(df['ProductId'])
		for index, item in enumerate(df['ProductId']):
			if item == result.index[0]:
				quantity -= 1
		df['ProductId'][result.index[0]] = quantity
	return result
