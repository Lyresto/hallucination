mask = (df['value'] < section_left) | (df['value'] > section_right)
sub_df = df[~mask]
average = sub_df['value'].mean()
df = df[mask]
df.loc['X'] = average
