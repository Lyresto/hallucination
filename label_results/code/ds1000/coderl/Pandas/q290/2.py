import pandas as pd
#df_a = pd.read_csv(path_a, sep=',')
#df_b = pd.read_csv(path_b, sep=',')
df_c = pd.merge(df_a, df_b, on='EntityNum')

#I don't think it is possible to have some of the unwanted columns in the final dataframe? 
#And I'm stuck with Pandas. 
#df_c = pd.merge(df_a, df_b, on='EntityNum')
