#SOLUTION END

x = []
y = []
for i, v in enumerate(a):
	x.append(i*v+b[i])
	y.append(c[i])

d = pd.DataFrame(x, index=y)

d.plot(x='b', y='a')
d.plot(x='c', y='d')

d.plot(x='a', y='c', color='r')
d.plot(x='d', y='a', color='b')

d.plot(x='b', y='d', color='g')
d.plot(x='c', y='d', color='b')

d.set_index('b')

d.plot(x='c', y='b', color='r')
d.plot(x='d', y='c', color='b')
d.set_index('c')

d.plot(x='c', y='d', color='g')
d.plot(x='b', y='c', color='r')

d.set_index('d')

d.plot(x='a', y='b', color='g')
d.plot(x='d', y='a', color='r')
