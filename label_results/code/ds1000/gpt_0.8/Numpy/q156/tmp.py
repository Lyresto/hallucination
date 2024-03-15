import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy.stats import rankdata
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(a):
    import numpy as np
    from scipy.stats import rankdata
    
    


def reverse_rankdata(a):
    ranks = rankdata(a).astype(int)
    max_rank = np.max(ranks)
    reverse_ranks = max_rank - ranks + 1
    return reverse_ranks

a = [1,2,3,4,3,2,3,4]
result = reverse_rankdata(a)
print(result)



result = f(a)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
