from itertools import permutations as p
import numpy as np

def permutation(probabilit, lista_elegir):
	np.random.shuffle(lista_elegir)
	return np.random.choice(lista_elegir, samples, probabilit)
	
def solution(lista_elegir, samples):
	return np.random.choice(lista_elegir, samples).tolist()
