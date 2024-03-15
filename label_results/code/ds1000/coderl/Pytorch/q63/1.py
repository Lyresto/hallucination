def solve(a, b):
	# a, b = map(zip, zip(*zip(*sorted(zip(a, b)))))
	return [list(x) for a, b in zip(a, b)][-2:]
