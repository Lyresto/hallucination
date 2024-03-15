min_date = df['dt'].min()
max_date = df['dt'].max()
idx = pd.date_range(min_date, max_date)
users = df['user'].unique()
result = pd.DataFrame({'dt': idx})
for user in users:
    user_df = df[df['user'] == user].set_index('dt')
    user_df = user_df.reindex(idx, fill_value=0)
    user_df.reset_index(inplace=True)
    user_df['user'] = user
    result = pd.concat([result, user_df[['user', 'dt', 'val']]], ignore_index=True)
