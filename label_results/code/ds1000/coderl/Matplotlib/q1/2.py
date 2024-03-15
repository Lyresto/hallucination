from itertools import chain
import numpy as np

x = np.random.rand(10)
y = np.random.rand(10)

res = list(chain(x, y))

sns.pairplot(res)
# SOLUTION END
