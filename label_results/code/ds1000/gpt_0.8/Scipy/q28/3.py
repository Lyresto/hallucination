To count the number of regions of cells that exceed a given threshold, we can use image segmentation techniques. One approach is to use the connected components labeling algorithm to label each connected region in the image.

Here's an example implementation using the `scipy.ndimage.label` function:

```python
import numpy as np
from scipy import ndimage

def count_regions_above_threshold(img, threshold):
    # Binarize the image based on the threshold
    binary_img = img > threshold
    
    # Label connected regions
    labeled_img, num_labels = ndimage.label(binary_img)
    
    # Return the number of labeled regions
    return num_labels

# Example usage
threshold = 0.75
num_regions = count_regions_above_threshold(img, threshold)
print("Number of regions above threshold:", num_regions)
```

In this example, `img` is the 2D numpy array containing the image data, and `threshold` is the value above which we consider a cell to be part of a region. The function `count_regions_above_threshold` returns the number of labeled regions above the threshold.

Note that we first binarize the image by comparing each pixel value to the threshold. We then use the `ndimage.label` function to label each connected region in the binary image. Finally, we return the number of labeled regions.