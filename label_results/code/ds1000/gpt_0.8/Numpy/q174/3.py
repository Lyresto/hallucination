import numpy as np
import pandas as pd

lat=np.array([[10, 20, 30],
              [20, 11, 33],
              [21, 20, 10]])

lon=np.array([[100, 102, 103],
              [105, 101, 102],
              [100, 102, 103]])

val=np.array([[17, 2, 11],
              [86, 84, 1],
              [9, 5, 10]])

df = pd.DataFrame({'lat': lat.flatten(), 'lon': lon.flatten(), 'val': val.flatten()})
df