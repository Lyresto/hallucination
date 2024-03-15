import pandas as pd
import numpy as np


np.random.seed(10)
data = {}
for i in [chr(x) for x in range(65,91)]:
    data['Col '+i] = np.random.randint(1,100,10)
df = pd.DataFrame(data)
list_of_my_columns = ['Col A', 'Col E', 'Col Z']
