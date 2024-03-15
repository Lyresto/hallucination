import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
probabilit, lista_elegir, samples = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from random import choice
from numpy import numpy as np




def rand_tuple(lista_elegir, probabilit):
    return np.random.choice(lista_elegir, samples, probabilit)




def result(lista_elegir, samples, probabilit):
    resultado = []
    for _ in range(samples):
        resultado.append(choice(lista_elegir, p=probabilit))
    return resultado



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
