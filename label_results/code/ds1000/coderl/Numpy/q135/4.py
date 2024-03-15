def unpackbits(n):
	b = bin(n)[2:]
	return [int(i) for i in b]
