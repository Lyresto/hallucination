import re
def parse_col_name(col_name):
	return re.sub('[a-zA-Z0-9]', "", col_name)
