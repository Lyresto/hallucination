import pandas as pd

s = pd.Series(['Name1', 'Name2', 'Name3'], index = ['2001', '2002', '2003', '2004', '2005', '2006'])
s.cumsum()
s.plot()
