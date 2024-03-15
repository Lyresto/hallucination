One way to achieve a 'highest to lowest' ranking of a list of values is by subtracting the rank from the maximum rank. Here's how you can do it:

```python
import numpy as np
from scipy.stats import rankdata

def reverse_rankdata(a):
    ranks = rankdata(a)
    max_rank = np.max(ranks)
    reverse_ranks = max_rank - ranks + 1
    return reverse_ranks.astype(int)

# Example usage
a = [1, 2, 3, 4, 3, 2, 3, 4]
result = reverse_rankdata(a)
print(result)
# Output: [7 6 3 1 3 6 3 1]
```

In this code, we first calculate the ranks using `rankdata()` function from scipy.stats. Then, we calculate the maximum rank using `np.max()`. Finally, we subtract each rank from the maximum rank and add 1 to get the 'highest to lowest' ranking.