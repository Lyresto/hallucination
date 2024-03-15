One way to solve this problem is by using a loop and iterating over the elements of A to compute the corresponding elements of B. Here is one possible implementation using pandas:

```python
B = pd.Series(index=A.index)

# Compute B[0]
B[0] = a * A[0]

# Compute B[t] for t > 0
for t in range(1, len(A)):
    B[t] = a * A[t] + b * B[t-1]
```

Alternatively, you can use the `numpy` library to vectorize the computation and avoid the loop:

```python
B = np.zeros_like(A)
B[0] = a * A[0]
B[1:] = a * A[1:] + b * B[:-1]
B = pd.Series(B, index=A.index)
```

Both of these implementations will give you the desired series B, computed recursively according to the given formula.