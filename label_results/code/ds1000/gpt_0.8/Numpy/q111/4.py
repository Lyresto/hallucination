To achieve the same functionality as the `sub2ind` function in MATLAB, you can use the following code in Python using NumPy:

```python
import numpy as np

def sub2ind(array_shape, rows, cols, slices):
    """
    Convert subscripts to linear indices in NumPy array.
    
    Parameters:
    - array_shape: shape of the array
    - rows: row subscripts
    - cols: column subscripts
    - slices: slice subscripts
    
    Returns:
    - linear indices corresponding to the subscripts
    """
    # Get the number of dimensions
    ndims = len(array_shape)
    
    # Convert subscripts to arrays
    rows = np.array(rows)
    cols = np.array(cols)
    slices = np.array(slices)
    
    # Calculate the linear indices
    linear_indices = rows + cols * array_shape[0] + slices * (array_shape[0] * array_shape[1])
    
    return linear_indices

# Example usage
dims = (3, 4, 2)
a = np.random.rand(*dims)
index = (1, 0, 1)

linear_index = sub2ind(dims, *index)
print(linear_index)
```

This will output `13`, which corresponds to the linear index `(2, 1, 2)` in MATLAB.

Note that the `sub2ind` function in MATLAB uses Fortran order, while NumPy uses C order. The code above assumes C order indexing. If you want to use Fortran order indexing, you can modify the calculation of `linear_indices` as follows:

```python
linear_indices = slices + cols * array_shape[2] + rows * (array_shape[1] * array_shape[2])
```

I hope this helps! Let me know if you have any further questions.