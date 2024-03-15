from random import choice
from itertools import product


def rand_choice(lista_elegir, samples, probabilit):
	probabilit = list(map(float, probabilit))
	return sum(choice(lista_elegir, k=1).count(i) * probabilit[i] for i in range(samples)) / sum(probabilit)
