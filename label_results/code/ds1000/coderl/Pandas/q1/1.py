def count_diff_type(df, other):
	diff_type = 0
	for i, type in enumerate(df["Type"]):
		if type == other["Type"]:
			diff_type += 1
	return diff_type
