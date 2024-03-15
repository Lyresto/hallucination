One approach to solving this problem efficiently is to use a combination of morphological operations available in the scipy.ndimage package. Specifically, we can use the binary_erosion and binary_dilation functions to identify isolated single cells and remove them.

Here's a possible solution:

```python
import numpy as np
import scipy.ndimage

# Input image
square = np.zeros((32, 32))
square[10:-10, 10:-10] = np.random.randint(1, 255, size=(12, 12))
np.random.seed(12)
x, y = (32 * np.random.random((2, 20))).astype(int)
square[x, y] = np.random.randint(1, 255, size=(20,))

# Find isolated single cells
square_binary = square > 0
square_eroded = scipy.ndimage.binary_erosion(square_binary)
isolated_cells = square_binary & ~square_eroded

# Remove isolated single cells
square[isolated_cells] = 0

# Output the resulting image
print(square)
```

This code first converts the input image to a binary image by setting all nonzero values to 1. It then applies the binary_erosion function to erode the binary image, which effectively removes all cells that are completely surrounded by 0s. By taking the logical AND between the original binary image and the eroded image, we obtain a mask of isolated single cells.

Finally, we set the corresponding elements in the original image to 0 using the mask of isolated cells. The resulting image will have all isolated single cells removed.

Note: The code assumes that `square` is a numpy array representing the image.