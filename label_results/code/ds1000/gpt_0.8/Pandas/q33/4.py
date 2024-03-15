# extract value columns
value_cols = [col for col in df.columns if col.startswith('val')]

# group by 'group' column and calculate mean for all value columns
result = df.groupby('group')[value_cols].mean().reset_index()

# add 'group_color' column back to the result
result = pd.merge(result, df[['group', 'group_color']].drop_duplicates(), on='group')

# re-arrange columns to match the original order
result = result[df.columns.tolist()]

result
