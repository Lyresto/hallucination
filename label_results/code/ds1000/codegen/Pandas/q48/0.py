df.loc[df['value'] < thresh, 'value'] = df.loc[df['value'] < thresh, 'value'].mean()
