def parse_first(s):
	try:
		while s[-1]!= '_':
			s = s[:-1]
		return s
	except:
		return s


def parse_last(s):
	try:
		while s[0]!= '_':
			s = s[1:]
		return s
	except:
		return ''
