# plot y over x
# do not show xticks of the plot
# SOLUTION END

df = pd.DataFrame({'x': x, 'y': y})
# print(df)
df.plot(x='x', y='y')
# SOLUTION START
df.plot(x='x', y='y', title='plot y over x')
# print(df)

# SOLUTION END
