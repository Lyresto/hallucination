import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, col, multiply_number = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def solve():
    col = int(input())
    a = list(map(float, input().split()))
    mult = a[col]
    c = 0
    s = []
    for i in range(len(a)):
        c += a[i]
        s.append(c)
    result = s
    print(result)




def __starting_point():
    solve()
__starting_point()



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
