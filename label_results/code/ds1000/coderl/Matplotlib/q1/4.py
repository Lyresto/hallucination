import numpy as np
import pandas as pd

# SOLUTION END
# x = np.random.rand(10)
# y = np.random.rand(10)
# plt.scatter(x, y)

x = pd.Series(x)
y = pd.Series(y)
sns.distplot(x, y, "y")
