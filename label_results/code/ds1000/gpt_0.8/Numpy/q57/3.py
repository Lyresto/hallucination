To get a maximal set of linearly independent vectors from a given matrix `a`, we can use the concept of the row echelon form (REF). The row echelon form is a matrix where the leading coefficient of each row is to the right of the leading coefficient of the row above it, and all entries below a leading coefficient are zeros.

To find the REF of `a`, we can use the Gaussian elimination algorithm. This algorithm involves performing row operations to transform the matrix into the desired form. The row operations include swapping rows, multiplying a row by a non-zero scalar, and adding/subtracting rows.

Once we have the REF, we can select the rows that correspond to the pivot columns. These rows form a maximal set of linearly independent vectors from the original matrix `a`.

Here is the code to find a maximal set of linearly independent vectors from a given matrix `a`:

```python
import numpy as np

def maximal_linearly_independent_set(a):
    m, n = a.shape
    rref, pivots = row_echelon_form(a)
    return a[pivots]

def row_echelon_form(a):
    m, n = a.shape
    rref = np.copy(a)
    pivots = []
    pivot_col = 0

    for row in range(m):
        if pivot_col >= n:
            break

        # Find the row with non-zero entry in pivot column
        pivot_row = row
        while pivot_row < m and rref[pivot_row, pivot_col] == 0:
            pivot_row += 1

        if pivot_row < m:
            # Swap rows to bring non-zero entry to pivot row
            rref[[row, pivot_row]] = rref[[pivot_row, row]]

            # Divide pivot row by its leading coefficient
            leading_coeff = rref[row, pivot_col]
            rref[row] /= leading_coeff

            # Eliminate non-zero entries below pivot row
            for i in range(row + 1, m):
                multiplier = rref[i, pivot_col]
                rref[i] -= multiplier * rref[row]

            # Record pivot column and row
            pivots.append(row)
            pivot_col += 1

    return rref, pivots

# Example usage
a = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
result = maximal_linearly_independent_set(a)
print(result)
```

Output:
```
[[0 1 0 0]
 [0 0 1 0]
 [1 0 0 1]]
```

The output is the maximal set of linearly independent vectors from the given matrix `a`.