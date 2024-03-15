import numpy as np
import pandas as pd

A = pd.Series(np.random.randn(10,))
a,b = 2,3

B = [0]

for i in range(1,len(A)):
	B.append(a*A[i]+b*B[i-1])
