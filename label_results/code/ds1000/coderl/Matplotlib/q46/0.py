# SOLUTION START
# SOLUTION START
# SOLUTION START

from itertools import chain

df = pd.DataFrame({'a':x, 'b':y})
xs = list(chain.from_iterable([df.a, df.b]))
ls = list(chain.from_iterable([df.a-df.b, df.b-df.a]))

sns.lmplot('a', 'b', data=xs, col='c', ls=ls)

# put legend in lower right
# SOLUTION END
