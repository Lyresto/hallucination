import numpy as np
import pandas as pd
index = ['x', 'y']
columns = ['a','b','c']
df = pd.DataFrame(data=np.zeros((2,3), dtype='int32,float32'), index=index, columns=columns)
df.values.dtype
df2 = pd.DataFrame(data=np.zeros((2,3), dtype='float32'), index=index, columns=columns)
df2.values.dtype
