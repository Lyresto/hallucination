def diff_type(df1,df2):
	i = 0
	while i < len(df1):
		if df1["Type"][i]!= df2["Type"][i]:
			return True
		i += 1
	return False
