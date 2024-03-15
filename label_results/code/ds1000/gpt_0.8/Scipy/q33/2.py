One possible solution to remove isolated single cells is to use the `scipy.ndimage.label` function to identify connected components in the image, and then filter out components with only a single pixel. Here's an example implementation:

```python
import numpy as np
from scipy.ndimage import label

# Input image array
image = np.array([[0, 0, 0], [0, 8, 0], [0, 0, 0]])

# Label connected components
labeled_image, num_labels = label(image)

# Filter out components with only a single pixel
for label_value in range(1, num_labels + 1):
    component = labeled_image == label_value
    if np.sum(component) == 1:
        image[component] = 0

# Output filtered image
print(image)
```

This will output:
```
[[0 0 0]
 [0 0 0]
 [0 0 0]]
```

The key idea is to use the `label` function to assign a unique label to each connected component in the image. Then, we iterate over each label and check if the component has only a single pixel. If so, we set all pixels in that component to 0 in the original image.