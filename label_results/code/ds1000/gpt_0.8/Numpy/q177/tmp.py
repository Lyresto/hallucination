import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, size = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def moving_window(arr, size):
    rows, cols = arr.shape
    padded_arr = np.pad(arr, ((1, 1), (1, 1)), mode='constant')
    result = []
    
    for i in range(rows):
        for j in range(cols):
            window = padded_arr[i:i+size[0], j:j+size[1]]
            result.append(window)
    
    return result

result = moving_window(a, size)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
