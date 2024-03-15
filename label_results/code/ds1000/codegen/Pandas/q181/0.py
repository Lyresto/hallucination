import pandas as pd
import numpy as np

dict = {'abc':'1/2/2003', 'def':'1/5/2017', 'ghi':'4/10/2013'}
df = pd.DataFrame({'Member':['xyz', 'uvw', 'abc', 'def', 'ghi'], 'Group':['A', 'B', 'A', 'B', 'B'], 'Date':[np.nan, np.nan, np.nan, np.nan, np.nan]})
