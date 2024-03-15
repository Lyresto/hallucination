To count the number of regions of cells that exceed a given threshold, we can use the following approach:

1. Create a binary mask where the cells that exceed the threshold are set to 1, and the rest are set to 0.
2. Use the `label` function from `scipy.ndimage` to label connected regions in the binary mask.
3. Count the number of unique labels in the labeled mask.

Here's the updated code:

```python
import numpy as np
from scipy import ndimage

np.random.seed(10)
gen = np.random.RandomState(0)
img = gen.poisson(2, size=(512, 512))
img = ndimage.gaussian_filter(img.astype(np.double), (30, 30))
img -= img.min()
img /= img.max()

def count_regions(img, threshold):
    binary_mask = img > threshold
    labeled_mask, num_regions = ndimage.label(binary_mask)
    return num_regions

threshold = 0.75
num_regions = count_regions(img, threshold)
print("Number of regions:", num_regions)
```

Running this code will give you the number of regions in the image that exceed the threshold.