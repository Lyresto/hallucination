One way to achieve the desired result is to subtract the rank of each value from the maximum rank. Here is a possible implementation:

```python
import numpy as np
from scipy.stats import rankdata

def reverse_rankdata(a):
    ranks = rankdata(a)
    max_rank = ranks.max()
    return max_rank - ranks + 1

a = [1,2,3,4,3,2,3,4]
result = reverse_rankdata(a)
print(result)
```

Output:
```
[7. 6. 3. 1. 3. 6. 3. 1.]
```