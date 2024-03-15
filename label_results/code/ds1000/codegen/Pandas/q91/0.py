import pandas as pd


index = pd.MultiIndex.from_tuples([('abc', '3/1/1994'), ('abc', '9/1/1994'), ('abc', '3/1/1995')],
                                 names=('id', 'date'))
df = pd.DataFrame({'x': [100, 90, 80], 'y':[7, 8, 9]}, index=index)
