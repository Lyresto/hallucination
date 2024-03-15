import pandas as pd
melt=lambda df,v:pd.melt(df,v,merge_vars=True)
