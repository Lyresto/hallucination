One way to achieve the desired ranking is to subtract the rank of each element from the maximum rank. Here's one possible implementation:

```python
import numpy as np
from scipy.stats import rankdata

def reverse_rankdata(a):
    ranks = rankdata(a).astype(int)
    max_rank = np.max(ranks)
    reverse_ranks = max_rank - ranks + 1
    return reverse_ranks

a = [1,2,3,4,3,2,3,4]
result = reverse_rankdata(a)
print(result)
```

This will give the output:

```
[7 6 3 1 3 6 3 1]
```

Explanation:
1. Use the `rankdata` function from `scipy.stats` to obtain the ranks of the elements in the list `a`.
2. Convert the ranks to integers using `astype(int)`.
3. Find the maximum rank in the list using `np.max(ranks)`.
4. Subtract each rank from the maximum rank and add 1 to get the reverse ranks.
5. Return the reverse ranks.

Note that in this implementation, ties are handled by assigning them the same rank.