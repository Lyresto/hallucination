import numpy as np

a = np.array([[1,0,3], [2,4,1]])
n = np.max(a) + 1

b = np.zeros((a.shape[0], n))
b[np.arange(a.shape[0])[:, np.newaxis], a] = 1
END SOLUTION

print(b)