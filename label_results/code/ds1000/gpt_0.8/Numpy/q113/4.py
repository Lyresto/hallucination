values = np.zeros((2,3), dtype={'names': columns, 'formats': ['int', 'float', 'float']})
df = pd.DataFrame(data=values, index=index, columns=columns)
df
