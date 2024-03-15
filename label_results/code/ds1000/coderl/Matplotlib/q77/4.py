# import pandas as pd
# df1 = pd.DataFrame({'x': x, 'y': y, 'z': z})
# df2 = pd.DataFrame({'x': x, 'y': y, 'z': z, 'a': a})
# df1.plot(kind='bar', x='y', y='x', z='z', a='a')
# df2.plot(kind='bar', x='z', y='y', a='a')
# return df1, df2

# plot x over y over z over a in two different subplots
# Set "X and Y" as a main title above the two subplots
# SOLUTION START
# df1, df2 = pd.DataFrame({'x': x, 'y': y, 'z': z, 'a': a}), pd.DataFrame({'x': x, 'y': y, 'z': z, 'a': a})
# df1.plot(kind='bar', x='y', y='x', z='z', a='a')
# df2.plot(kind='bar', x='z', y='y', z='x', a='a')
# return df1, df2

# p1 = df1.plot(kind='bar', x='x', y='y', z='z', a='a')
# p2 = df2.plot(kind='bar', x='z', y='y', z='x', a='a')

# SOLUTION END
