import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
probabilit, lista_elegir, samples = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
probabilit = [0.333, 0.333, 0.333]
lista_elegir = [(3, 3), (3, 4), (3, 5)]
samples = 1000
np.random.choice(lista_elegir, samples, probabilit)

#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
