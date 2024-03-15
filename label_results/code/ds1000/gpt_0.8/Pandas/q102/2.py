### Solution 1: Using the `.replace()` method

You can use the `.replace()` method to replace the `'&AMP;'` with `'&'` in all columns of the DataFrame. 

Here's how you can do it:

```python
import pandas as pd

# Create example DataFrame
example_df = pd.DataFrame({'A': ['Good &AMP; bad', 'BB', 'CC', 'DD', 'Good &AMP; bad'], 
                           'B': range(5), 
                           'C': ['Good &AMP; bad'] * 5})

# Function to replace '&AMP;' with '&'
def replace_amp(df):
    return df.replace('&AMP;', '&', regex=True)

# Apply the function to the DataFrame
result = replace_amp(example_df)
```

This will replace all occurrences of `'&AMP;'` with `'&'` in all columns of the DataFrame.

### Solution 2: Using the `.applymap()` method

Alternatively, you can use the `.applymap()` method to apply a custom function to each element of the DataFrame.

Here's how you can do it:

```python
import pandas as pd

# Create example DataFrame
example_df = pd.DataFrame({'A': ['Good &AMP; bad', 'BB', 'CC', 'DD', 'Good &AMP; bad'], 
                           'B': range(5), 
                           'C': ['Good &AMP; bad'] * 5})

# Custom function to replace '&AMP;' with '&'
def replace_amp(x):
    return x.replace('&AMP;', '&')

# Apply the function to each element of the DataFrame
result = example_df.applymap(replace_amp)
```

This will replace all occurrences of `'&AMP;'` with `'&'` in all columns of the DataFrame.

Both solutions will produce the same result. Choose the one that suits your preference.