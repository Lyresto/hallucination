from collections import defaultdict

def exp(x, y, p):
	return x ** y * p ** (1 + p)

def exp_dict(x, y, p):
	d = defaultdict(list)
	for i, v in enumerate(x):
		d[v].append(exp(v, y, p))
	return d
	
def add_exp(df, key, p):
	d = exp_dict(df, key, p)
	for v, z in d.items():
		df[key] = z
