import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, pos, element = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(a, pos=2, element = 66):
    import numpy as np
    
    


def insert_element(array, index, element):
    return np.insert(array, index, element)

example_a = np.asarray([1, 2, 3, 4])
new_a = insert_element(example_a, 2, 66)
print(new_a)



result = f(a, pos, element)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
