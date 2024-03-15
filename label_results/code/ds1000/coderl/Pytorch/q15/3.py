import numpy as np
import torch
idx, B = load_data()
C = torch.LongTensor([[j[i] for i in range(len(idx))] for j in B])
