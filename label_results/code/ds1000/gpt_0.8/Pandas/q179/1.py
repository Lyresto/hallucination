result = df.loc[df.groupby(['Sp','Mt'])['count'].idxmin()]
