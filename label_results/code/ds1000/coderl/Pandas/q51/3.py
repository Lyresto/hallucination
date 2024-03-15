import pandas as pd
result = pd.DataFrame({k: [i**k for i,k in enumerate(df[k])] for k in df})
