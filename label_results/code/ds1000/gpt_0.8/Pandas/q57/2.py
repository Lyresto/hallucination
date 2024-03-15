min_date = df['dt'].min()
max_date = df['dt'].max()
new_df = pd.DataFrame({'dt': pd.date_range(min_date, max_date), 'user': df['user'].unique()})
result = pd.merge(new_df, df, on=['dt', 'user'], how='left').fillna(0)
