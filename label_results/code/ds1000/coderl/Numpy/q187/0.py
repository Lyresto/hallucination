import numpy as np
a = np.array([[1,0,2,3],[0,5,3,4],[2,3,2,10],[3,4, 10, 7]])
b = np.linalg.solve(a,a.T)
print((b))
