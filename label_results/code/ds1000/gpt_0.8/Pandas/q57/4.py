min_date = df['dt'].min()
max_date = df['dt'].max()
date_range = pd.date_range(min_date, max_date)

result = pd.DataFrame({'dt': date_range})
result['user'] = df['user'].unique()[0]
result = result.merge(df, on=['user', 'dt'], how='left').fillna(0)
