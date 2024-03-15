from itertools import zip_longest

# https://www.youtube.com/watch?v=DY4u7_0_c
# https://www.youtube.com/watch?v=JJhHn4u8
df = pd.DataFrame({'x': x, 'y': y})
xs, ys = zip_longest(df['x'], df['y'], fillvalue=0)

# in plt.plot(xs, ys), use a plus marker, give it a thickness of 7
# SOLUTION END
