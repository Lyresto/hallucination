import pandas as pd
df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B'], 'group_color' : ['green', 'green', 'green', 'blue', 'blue'], 'val1': [5, 2, 3, 4, 5], 'val2' : [4, 2, 8, 5, 7],'val3':[1,1,4,5,1]})
df.groupby('group').agg({'group_color': 'first', 'val1':'sum', 'val2':'sum', 'val3':'sum'})
print(df.groupby('group').agg({'group_color':'sum', 'val1':'sum', 'val2':'sum', 'val3':'sum'}))
