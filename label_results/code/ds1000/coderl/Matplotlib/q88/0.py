def f():
	p = pd.Series(range(1, 10))
	return [str(i) for i in p.plot(kind='bar')]
