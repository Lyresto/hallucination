import numpy as np
import pandas as pd
import torch
t, idx = load_data()
print(t)
print(idx)
t = torch.from_numpy(np.array(t))
print(t)
ans = np.zeros((len(idx)+1, len(idx)+1), dtype=np.int64)

for i,j in enumerate(idx):
	ans[i,j] = t[j]

print(ans)
