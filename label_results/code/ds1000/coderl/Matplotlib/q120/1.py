from collections import Counter

df = pd.DataFrame({'x':x, 'y':y})

count = Counter(df['x'])

for i in count:
	print(i, count[i])
