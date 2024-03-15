import numpy as np
df = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
cols = df.columns
result = np.array(df[df.c > 0.45])
