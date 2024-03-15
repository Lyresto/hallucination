from numpy import array, sum
from torch import *

t1 = load_data()
t2 = load_data()

print((sum(array(t1[1]).values!= array(t2[1]).values)))
