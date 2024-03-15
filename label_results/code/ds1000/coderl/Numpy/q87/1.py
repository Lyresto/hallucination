import torch
from numpy import array

a = array('i', a)
a_pt = torch.from_numpy(a.reshape(5, 5))
