Here's a simple and efficient way to make a sparse scipy matrix symmetric:

1. Convert the matrix to a csr_matrix.
2. Create a new matrix by adding its transpose to itself.
3. Divide the resulting matrix by 2 to average the values.
4. Convert the resulting matrix back to the desired sparse format.

Here's the code to implement this:

```python
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix

def make_symmetric(matrix):
    # Convert matrix to csr_matrix
    matrix = csr_matrix(matrix)

    # Add the transpose to the matrix
    matrix = matrix + matrix.T

    # Divide the matrix by 2 to average the values
    matrix = matrix / 2

    # Convert the matrix back to the desired sparse format
    matrix = matrix.asformat(matrix.format)

    return matrix
```

You can use this function to make your lil_matrix symmetric:

```python
# Create a lil_matrix
sA = lil_matrix((10, 10))

# Populate the matrix

# Make the matrix symmetric
sA = make_symmetric(sA)
```

This will efficiently make the matrix symmetric without the need to fill in both [row, col] and [col, row] at the same time.