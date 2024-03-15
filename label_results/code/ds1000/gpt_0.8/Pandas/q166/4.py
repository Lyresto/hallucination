import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[1,1,1,2,2,2,3,3,3], 'b':[12,13,23,22,23,24,30,35,55]})

result = df.groupby('a').b.agg(mean=np.mean, std=np.std)
result