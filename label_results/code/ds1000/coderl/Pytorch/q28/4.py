from numpy import zeros
import torch
a = torch.rand((10, 1000, 96))
lengths = torch.randint(1000, (10,))
a = a.unsqueeze(1)
a[lengths, :, :] = 0
