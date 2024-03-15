To count the number of regions of cells that exceed a given threshold, you can use the following approach:

1. Create a binary mask where each cell is True if its value exceeds the threshold, and False otherwise. You can do this by comparing the array with the threshold value:

   ```python
   mask = img > threshold
   ```

2. Use the `label` function from `scipy.ndimage` to label connected regions in the binary mask:

   ```python
   labeled_mask, num_regions = ndimage.label(mask)
   ```

   This will assign a unique label to each connected region and return the total number of regions.

3. Print the number of regions:

   ```python
   print("Number of regions:", num_regions)
   ```

Putting it all together, the function `count_regions` can be defined as follows:

```python
import numpy as np
from scipy import ndimage

def count_regions(img, threshold):
    mask = img > threshold
    labeled_mask, num_regions = ndimage.label(mask)
    return num_regions

# Example usage
img = np.random.rand(512, 512)  # Replace with your actual image
threshold = 0.75
num_regions = count_regions(img, threshold)
print("Number of regions:", num_regions)
```

This will output the number of regions in the image that exceed the threshold.