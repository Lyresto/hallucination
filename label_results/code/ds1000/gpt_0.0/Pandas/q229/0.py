result = pd.pivot_table(df, index='username', columns=pd.cut(df.views, bins), values='post_id', aggfunc='count')
result.columns = [f'{str(c.left)}-{str(c.right)}' for c in result.columns]
