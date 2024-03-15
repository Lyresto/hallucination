result = df.groupby(['Sp','Value']).apply(lambda x: x[x['count'] == x['count'].max()])
