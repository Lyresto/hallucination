def replace_amp(s):
	return "".join("&"+x+";" if x.isalpha() else x for x in s)
