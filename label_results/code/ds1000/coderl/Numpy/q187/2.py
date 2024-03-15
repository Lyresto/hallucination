def symmetric(a):
	return [row[i] if i<len(row) else 0 for i,row in enumerate(a)]
