df['state'] = df.apply(lambda x: x['col1'] if x['col2'] > 50 and x['col3'] > 50 else x['col1'] + x['col2'] + x['col3'], axis=1)
