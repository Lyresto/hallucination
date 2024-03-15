df[['fips', 'row']] = df['row'].str.split(' ', 1, expand=True)
