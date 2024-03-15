To replace '&AMP;' with '&' from all columns in a pandas DataFrame, you can use the `replace()` function with the `regex` parameter set to `True`. Here's how you can do it:

```python
import pandas as pd

example_df = pd.DataFrame({'A': ['Good &AMP; bad', 'BB', 'CC', 'DD', 'Good &AMP; bad'], 'B': range(5), 'C': ['Good &AMP; bad'] * 5})

def f(df=example_df):
    df = df.replace('&AMP;', '&', regex=True)
    return df

result = f(example_df)
print(result)
```

Output:
```
              A  B              C
0  Good & bad    0  Good & bad  
1  BB           1  Good & bad  
2  CC           2  Good & bad  
3  DD           3  Good & bad  
4  Good & bad    4  Good & bad  
```

The `replace()` function replaces all occurrences of '&AMP;' with '&' in all columns of the DataFrame. Setting `regex=True` allows you to use regular expressions for pattern matching.