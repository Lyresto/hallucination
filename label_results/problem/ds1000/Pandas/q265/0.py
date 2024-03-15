result = df.columns[df.iloc[[0,8]].T.apply(lambda x: x[0]==x[1] if not (np.isnan(x[0]) or np.isnan(x[1])) else True).values]
