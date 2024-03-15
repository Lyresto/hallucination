import numpy as np
df = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
print(df)
print(np.array(df[df.c > 0.45]))
