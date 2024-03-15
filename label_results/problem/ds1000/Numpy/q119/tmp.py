import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
probabilit, lista_elegir, samples = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.random.choice(np.arange(len(lista_elegir)), size=samples, p=probabilit)
result = [lista_elegir[i] for i in result]

#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
