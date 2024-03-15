def rand_select(df):
	s = df.sample(int(len(df)*0.8), random_state=0)
	res = {}
	for i, row in enumerate(s):
		res["UserId"] = row["UserId"]
		res["ProductId"] = row["ProductId"]
		res["Quantity"] = row["Quantity"]
	return res
