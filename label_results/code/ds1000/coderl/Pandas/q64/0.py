def solve():
	import pandas as pd
	s = pd.concat([pd.DataFrame({'name': ['Aaron', 'Aaron', 'Aaron', 'Brave', 'Brave', 'David'],
						  'a': [3, 3, 3, 4, 3, 5],
						  'b': [5, 6, 6, 6, 6, 1],
						  'c': [7, 9, 10, 0, 1, 4]}) for _ in range(10)],
				 keys=['name','a'])
	return s.replace(dict.fromkeys(s.a),str(id(s.a[0])))
