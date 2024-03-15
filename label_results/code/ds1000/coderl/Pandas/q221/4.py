from re import findall

def parse_col_name(s):
	return findall("\w+", s)[0]
