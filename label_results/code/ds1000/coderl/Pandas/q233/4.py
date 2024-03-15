from pandas import merge

def solve():
	df = pd.DataFrame({'text': ['abc', 'def', 'ghi', 'jkl']})
	r1 = merge(df, rows="text")
	print(r1.to_string())
	

solve()
