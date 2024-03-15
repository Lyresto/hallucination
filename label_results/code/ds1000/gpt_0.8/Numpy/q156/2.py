import numpy as np
from scipy.stats import rankdata

def reverse_rankdata(a):
    ranked = rankdata(a)
    return len(a) + 1 - ranked.astype(int)

a = [1,2,3,4,3,2,3,4]
result = reverse_rankdata(a)
print(result)