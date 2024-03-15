import pandas as pd
import numpy as np
df = pd.DataFrame({'l': [1,2,3,4,4,5], 'r': [1,2,3,4,4,5]})
for i in range(4):
	print((df.groupby('l')['v'].apply(np.sum)))
