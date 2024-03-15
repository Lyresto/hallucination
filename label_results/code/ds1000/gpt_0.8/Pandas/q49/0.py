mask = (df['value'] < section_left) | (df['value'] > section_right)
avg = df.loc[mask, 'value'].mean()
df.loc[~mask, 'value'] = avg
df = df.groupby(df.index).first() # remove duplicates
df = df.reset_index()
df.loc[df['value'] == avg, 'lab'] = 'X'
df = df.groupby('lab').sum()
