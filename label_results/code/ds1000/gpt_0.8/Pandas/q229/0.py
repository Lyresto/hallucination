result = df.groupby(['username', pd.cut(df['views'], bins)]).size().unstack().fillna(0)
result