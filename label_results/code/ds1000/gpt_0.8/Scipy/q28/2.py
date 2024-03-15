To count the number of regions of cells that exceed a given threshold, you can use the following code:

```python
import numpy as np
from scipy import ndimage

def count_regions(img, threshold):
    # Create a binary mask of cells that exceed the threshold
    mask = img > threshold
    
    # Label connected regions in the mask
    labels, num_regions = ndimage.label(mask)
    
    return num_regions

# Example usage
num_regions = count_regions(img, 0.75)
print("Number of regions:", num_regions)
```

This code uses the `ndimage.label` function from the `scipy` library to label connected regions in the binary mask. The `count_regions` function takes as input the image array and the threshold value, and returns the number of regions that exceed the threshold.