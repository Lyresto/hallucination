from numpy import zeros
import numpy as np
from pandas import pd
from torch import rand
a = torch.rand((10, 1000, 96))
lengths =  torch.randint(1000,(10,))
a = a.unsqueeze(2).contiguous()
a = a.numpy()

#BEGIN SOLUTION
zeros_arr = np.zeros(a.shape)
for i in range(10):
	zeros_arr[lengths[i, :], i, :] = 0
a = a.numpy().cumsum(1).contiguous()
a = a.numpy()
#END SOLUTION
