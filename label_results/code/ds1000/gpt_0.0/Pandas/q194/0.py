import dask.dataframe as dd
from dask import compute, delayed

df = dd.from_pandas(df, npartitions=2)

def split_rows(row):
    var1 = row['var1']
    var2 = row['var2'].split(',')
    return [(row['id'], var1, v) for v in var2]

new_rows = []
for _, row in df.iterrows():
    new_rows.extend(split_rows(row))

result = dd.from_delayed(new_rows, meta=('id', 'var1', 'var2'))
result = result.set_index('id')
