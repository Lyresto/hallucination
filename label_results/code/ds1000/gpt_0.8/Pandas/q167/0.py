import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[12,13,23,22,23,24,30,35,55], 'b':[1,1,1,2,2,2,3,3,3]})

stdMean = lambda x: pd.Series({'mean': np.mean(x), 'std': np.std(x)})
result = df.groupby('b')['a'].apply(stdMean)
print(result)
