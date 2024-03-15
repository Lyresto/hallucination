from itertools import cycle, chain

def plot(i):
	x = cycle(range(10))
	y = cycle(range(10))
	p1, p2 = zip(*[[p.plot(x, y) for p in chain([p1, p2], [p1, p2])] * 2])
	return [x for _, x in p1]
