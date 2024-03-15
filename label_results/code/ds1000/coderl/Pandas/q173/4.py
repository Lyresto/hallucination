import pandas as pd
def sort_series(s):
	s = list(s.values)
	s.sort()
	s.sort(key=s.index)
	return s
