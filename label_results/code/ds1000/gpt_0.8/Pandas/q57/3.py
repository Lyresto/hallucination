min_date = df['dt'].min()
max_date = df['dt'].max()
date_range = pd.date_range(min_date, max_date)
users = df['user'].unique()

new_df = pd.DataFrame(columns=['dt', 'user', 'val'])

for user in users:
    user_df = df[df['user']==user].set_index('dt')
    user_range = date_range.to_series().apply(lambda x: x.strftime('%Y-%m-%d'))
    user_df = user_df.reindex(user_range, fill_value=0).reset_index()
    user_df['user'] = user
    new_df = pd.concat([new_df, user_df])

new_df = new_df[['dt', 'user', 'val']]
new_df['dt'] = pd.to_datetime(new_df['dt'])
new_df = new_df.sort_values(['user', 'dt'])
