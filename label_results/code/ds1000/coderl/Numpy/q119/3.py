from itertools import product
from numpy import random


def choice(lista_elegir, samples, probabilit):
	p = list(map(lambda x: 1 - x, probabilit))
	result = [tuple(x) for x in
			  random.choices(lista_elegir, samples, p) if all(x == y for x, y in result)]
	try:
		return result[0]
	except IndexError:
		return tuple(result[0])
