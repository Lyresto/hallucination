import numpy as np
import scipy.ndimage
square = np.zeros((32, 32))
np.random.seed(12)
x, y = (32*np.random.random((2, 20))).astype(int)
square[x, y] = np.random.randint(1, 255, size = (20,))
square = square.astype(int)
res = scipy.ndimage.binary_fill_holes(square)
