Here's a possible solution to count the number of regions of cells which value exceeds the given threshold:

```python
import numpy as np
from scipy import ndimage

def count_regions(img, threshold):
    # Create a binary image where cells above the threshold are 1 and below are 0
    binary_img = (img > threshold).astype(int)
    
    # Label the connected regions in the binary image
    labeled_img, num_regions = ndimage.label(binary_img)
    
    return num_regions

# Example usage
threshold = 0.75
num_regions = count_regions(img, threshold)
print("Number of regions:", num_regions)
```

In this solution, we first create a binary image where cells above the threshold are assigned a value of 1 and cells below are assigned a value of 0. We then use the `ndimage.label` function from SciPy to label the connected regions in the binary image. The function returns the labeled image and the number of regions. We can then simply print the number of regions to get the desired result.