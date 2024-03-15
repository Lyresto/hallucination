import pandas as pd
import numpy as np

a = np.array(pd.read_csv(path_a, sep=','))
b = np.array(pd.read_csv(path_b, sep=','))
c = pd.merge(a, b, on='EntityNum')
print(c)
