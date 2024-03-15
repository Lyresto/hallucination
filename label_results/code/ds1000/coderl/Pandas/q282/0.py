import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=list('ABA'))
df.rename(columns={df.columns[-1]: 'Test'}, inplace=True)
result =... # put solution in this variable
