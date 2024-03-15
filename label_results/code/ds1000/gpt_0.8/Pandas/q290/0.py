import pandas as pd

df_a = pd.DataFrame({'EntityNum':[1001.01,1002.02,1003.03],'foo':[100,50,200]})
df_b = pd.DataFrame({'EntityNum':[1001.01,1002.02,1003.03],'a_col':['alice','bob','777'],'b_col':[7,8,9]})

result = pd.merge(df_a[['EntityNum', 'foo']], df_b[['EntityNum', 'b_col']], on='EntityNum')
result