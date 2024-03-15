def f(x=example_x):
	decode_x = lambda bytes_: [decode(s) for s in bytes_]
	return decode_x(x)

def decode(s):
	return s.decode('utf-8')
