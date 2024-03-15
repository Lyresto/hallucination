import numpy as np
#solving this problem
x = np.arange(10)
y = np.arange(10)
z = x*y
a = x + y

df = pd.DataFrame({'a': a, 'b': z})
df['c'].plot.bar(y_order=0)
#solving the next one
