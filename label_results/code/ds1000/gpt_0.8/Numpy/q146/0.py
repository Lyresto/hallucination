import numpy as np
a = np.array([[0, 1], [2, 1], [4, 8]])
mask = np.equal(a, np.min(a, axis=1, keepdims=True))
END SOLUTION
mask