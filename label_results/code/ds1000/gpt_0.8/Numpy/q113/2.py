values = np.zeros((2,3), dtype=[('a', 'int32'), ('b', 'float32'), ('c', 'float32')])
df = pd.DataFrame(data=values, index=index, columns=columns)
df
