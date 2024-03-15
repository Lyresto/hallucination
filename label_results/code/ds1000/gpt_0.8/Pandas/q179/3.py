df_grouped = df.groupby(['Sp','Mt'])
result = df.loc[df_grouped['count'].idxmin()]
