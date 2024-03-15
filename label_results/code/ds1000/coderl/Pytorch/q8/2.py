def convert_to_df(px):
	for i in range(6):
		px[str(i)] = px[str(i)].astype(float).apply(lambda x: str(x.item()), axis=1)
	return px
