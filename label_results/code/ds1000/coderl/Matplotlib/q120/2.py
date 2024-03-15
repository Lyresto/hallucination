df = pd.DataFrame({'x': x, 'y': y})

# SOLUTION END

f, ax = plt.subplots()
df['y'].plot(f, ax=ax)
f.suptitle('Title', size=20)
f.set_facecolor('0.5')

# SOLUTION START
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
