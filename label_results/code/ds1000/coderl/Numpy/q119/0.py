from random import choice
from numpy import numpy as np

def rand_tuple(lista_elegir, probabilit):
	return np.random.choice(lista_elegir, samples, probabilit)

def result(lista_elegir, samples, probabilit):
	resultado = []
	for _ in range(samples):
		resultado.append(choice(lista_elegir, p=probabilit))
	return resultado
