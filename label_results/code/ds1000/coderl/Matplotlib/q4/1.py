# SOLUTION END


def linesty(x, y):
	# SOLUTION START
	n, df = len(x), pd.DataFrame({"x": x, "y": y})
	for i in range(n):
		df["y"] = df["x"] + df["y"].mean()
	return df.plot()
