One way to achieve the desired result is to subtract the ranked array from the maximum rank plus one. Here's how you can do it:

```python
import numpy as np
from scipy.stats import rankdata

example_a = [1,2,3,4,3,2,3,4]

def f(a = example_a):
    ranked_array = rankdata(a).astype(int)
    max_rank = np.max(ranked_array)
    result = (max_rank + 1) - ranked_array
    return result

result = f()
print(result)
```

Output:
```
[7 6 3 1 3 6 3 1]
```

Explanation:
1. Rank the array using `rankdata(a).astype(int)`.
2. Find the maximum rank using `np.max(ranked_array)`.
3. Subtract the ranked array from `(max_rank + 1)` to get the desired result.