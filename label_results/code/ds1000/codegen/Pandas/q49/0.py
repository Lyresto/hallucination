import pandas as pd

df = pd.DataFrame({'lab':['A', 'B', 'C', 'D', 'E', 'F'], 'value':[50, 35, 8, 5, 1, 1]})
df = df.set_index('lab')
section_left = 4
section_right = 38

df = df.loc[df['value'] > section_left]
df = df.loc[df['value'] < section_right]

df = df.loc[df['value'] == section_left]
df = df.loc[df['value'] == section_right]

df = df.loc[df['value'] == section_left]
df = df.loc[df['value'] == section_right]

df = df.loc[df['value'] == section_left]
df = df.loc[df['value'] == section_right]
