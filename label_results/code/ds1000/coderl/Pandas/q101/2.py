def replace_it(s):
	for i in range(len(s)):
		if s[i] == "&lt;":
			s[i] = "<"
	return s
