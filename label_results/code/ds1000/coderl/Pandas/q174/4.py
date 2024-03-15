import pandas as pd
s = pd.Series([1,1,1,1,1,1,1,1,1,1,1,1,1,0.98,0.93],
	index=['146tf150p','havent','home','okie','thanx','er','anything','lei','nite','yup','thank','ok','where','beerage','anytime','too','done','645','tick','blank'])
# get the first value at a time
df = s.sort_values(by='value', ascending=True)
print(df)
