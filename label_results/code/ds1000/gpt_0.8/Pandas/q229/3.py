result = df.groupby(['username', pd.cut(df['views'], bins)])['views'].count().unstack().fillna(0).astype(int)
