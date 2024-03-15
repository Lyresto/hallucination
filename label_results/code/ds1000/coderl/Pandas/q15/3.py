import re

def expand(keys, df):
	pattern = re.compile(r'\[([a-z]+)\]: \[([0-9]+)\]\Z')
	result = []
	for k,v in df.items():
		match = pattern.search(v)
		if match:
			result.append([k,v.replace(match.group(1),'none').replace(match.group(2),'none'), match.group(3)])
	return result
