min_date = df['dt'].min()
max_date = df['dt'].max()

dates = pd.date_range(start=min_date, end=max_date, freq='D')
users = df['user'].unique()

expanded_df = pd.DataFrame({'dt': dates})

for user in users:
    user_df = df[df['user'] == user]
    merged_df = pd.merge(expanded_df, user_df, on='dt', how='left')
    merged_df['val'] = merged_df['val'].fillna(0)
    merged_df['user'] = merged_df['user'].fillna(user)
    result = merged_df[['dt', 'user', 'val']]
