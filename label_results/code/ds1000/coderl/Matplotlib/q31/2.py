# SOLUTION END
import numpy as np
import pandas as pd
import seaborn as sns

x = np.random.randn(10)
y = x

p = pd.Series(y)
p.plot.scatter(x, y)
