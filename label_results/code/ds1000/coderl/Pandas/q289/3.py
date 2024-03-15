import pandas as pd
df_a = pd.read_csv(path_a, sep=',')
df_b = pd.read_csv(path_b, sep=',')
df_c = pd.merge(df_a, df_b, on='EntityNum')
print(df_c)
