min_date = df['dt'].min()
max_date = df['dt'].max()
dates = pd.date_range(start=min_date, end=max_date)
users = df['user'].unique()
new_df = pd.DataFrame({'dt': dates})
for user in users:
    user_df = df[df['user']==user]
    user_df = user_df.set_index('dt')
    user_df = user_df.reindex(dates)
    user_df['user'] = user
    user_df['val'] = user_df['val'].fillna(0)
    new_df = pd.concat([new_df, user_df.reset_index()], axis=0)
new_df = new_df[['dt', 'user', 'val']]
