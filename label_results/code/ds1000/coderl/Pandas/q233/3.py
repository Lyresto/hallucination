import pandas as pd
from itertools import groupby

def solve():
	df = pd.DataFrame({'text': ['abc', 'def', 'ghi', 'jkl']})
	text_list = ['abc', 'def', 'ghi', 'jkl']
	text_groups = [''.join(grp) for key, grp in groupby(text_list)]
	result = pd.DataFrame({'text': text_groups})
	return result

def __starting_point():
	result = solve()
	print(result)
__starting_point()
