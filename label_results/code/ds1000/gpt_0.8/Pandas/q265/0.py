result = df.iloc[[0, 8]].T[df.iloc[0] == df.iloc[8]].index.tolist()
