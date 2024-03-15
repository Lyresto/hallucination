One way to find a maximal set of linearly independent vectors from a given matrix is by performing a rank calculation. The rank of a matrix is the maximum number of linearly independent rows or columns in the matrix.

To find the maximal set of linearly independent vectors, we can perform the following steps:

1. Transpose the matrix if necessary. In this case, the given matrix `a` is already in row echelon form, so no transposition is needed.

2. Calculate the rank of the matrix using the `numpy.linalg.matrix_rank()` function.

3. Select the first `rank` number of rows or columns as the maximal set of linearly independent vectors.

Here is the code to perform these steps:

<code>
import numpy as np

# Given matrix
a = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])

# Calculate the rank of the matrix
rank = np.linalg.matrix_rank(a)

# Select the first 'rank' number of rows/columns as the maximal set of linearly independent vectors
result = a[:rank]

print(result)
