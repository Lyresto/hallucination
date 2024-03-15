# Option 1: use filter to select columns that start with "val"
result = df.groupby('group').filter(lambda x: 'val' in x.columns).groupby('group').sum().reset_index()

# Option 2: use iloc to select columns that are not the first two
result = df.groupby('group').iloc[:, 2:].sum().reset_index()

# Option 3: use drop to remove non-value columns and sum remaining columns
result = df.drop(['group', 'group_color'], axis=1).groupby(df['group']).sum().reset_index()
