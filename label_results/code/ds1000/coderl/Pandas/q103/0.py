import re

def replace_amp(s):
	return re.sub(r'(?<= )(Good|Bad)(?= )', "&', s)
