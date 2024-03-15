result = df.groupby(['Sp', 'Mt']).filter(lambda x: x['count'] == x['count'].min())
