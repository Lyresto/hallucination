def sort_series(s):
	return s.sort_values(by=lambda x: s.index.get(x))
