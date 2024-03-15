You can use the `scipy.ndimage.label` function to label each connected region in the image array. Then, you can use `scipy.ndimage.find_objects` to get the bounding box for each labeled region. Finally, you can iterate over the bounding boxes and check if any of them have a width and height of 1. If they do, you can set the corresponding region in the original array to 0. Here's an example implementation:

```python
import numpy as np
import scipy.ndimage

# Example image array
square = np.zeros((32, 32))
square[10:-10, 10:-10] = np.random.randint(1, 255, size=(12, 12))
np.random.seed(12)
x, y = (32*np.random.random((2, 20))).astype(int)
square[x, y] = np.random.randint(1, 255, size=(20,))

# Label connected regions
labels, num_features = scipy.ndimage.label(square)

# Find bounding boxes for labeled regions
bounding_boxes = scipy.ndimage.find_objects(labels)

# Iterate over bounding boxes and remove isolated single cells
for bbox in bounding_boxes:
    min_x, max_x, min_y, max_y = bbox[0].start, bbox[0].stop, bbox[1].start, bbox[1].stop
    width = max_x - min_x
    height = max_y - min_y
    if width == 1 and height == 1:
        square[bbox] = 0

print(square)
```

This will output the image array with isolated single cells removed.