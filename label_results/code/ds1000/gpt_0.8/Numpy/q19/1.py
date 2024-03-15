import numpy as np
a = np.array([[10,50,30],[60,20,40]])
result = np.unravel_index(np.argmin(a), a.shape)
result