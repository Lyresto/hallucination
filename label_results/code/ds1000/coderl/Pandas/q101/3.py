import re
def replace_with_lt(s):
	return re.sub('[a-z]', "<", s)
