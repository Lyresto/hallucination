import pandas as pd

# df = pd.read_csv(data, sep=' ', index_col = 0)
df = pd.read_csv(io.StringIO("""
rs    alias  chrome  poston
TP3      A/C      0    3   
TP7      A/T      0    7   
TP12     T/A      0   12  
TP15     C/A      0   15 
TP18     C/T      0   18
""")).set_index('rs')

def extract_rows(df, rows):
	return df.select(rows)
