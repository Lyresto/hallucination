#!/usr/bin/env python3

def f(df, filt):
	res = df.copy()
	for i, v in df.index.items():
		if v:
			for j, c in filt.items():
				if not c:
					continue
				if i!= j:
					res[i] = None
	return res

def __starting_point():
	f(f(f(pd.DataFrame({'a': [1,1,1,2,2,2,3,3,3],
							  'b':[1,2,3,1,2,3,1,2,3],
							  'c':range(9)}).set_index(['a', 'b'])),
		pd.Series({1:True, 2:False, 3:True}))
__starting_point()
