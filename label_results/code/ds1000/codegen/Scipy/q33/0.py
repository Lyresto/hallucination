import numpy as np
import scipy.ndimage
square = np.zeros((32, 32))
square[10:-10, 10:-10] = np.random.randint(1, 255, size = (12, 12))
np.random.seed(12)
x, y = (32*np.random.random((2, 20))).astype(int)
square[x, y] = np.random.randint(1, 255, size = (20,))

