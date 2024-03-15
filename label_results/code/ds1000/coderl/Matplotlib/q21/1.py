from math import sin, pi
def f(x):
	return sin((x*2*pi)/10)
sns.distplot(f(x), 'cos')
sns.distplot(f(x),'sin')
sns.distplot(f(x), 'x')
sns.distplot(f(x), 'log')
