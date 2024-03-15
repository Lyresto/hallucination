import numpy as np
import scipy.ndimage

def remove_isolated_cells(image):
    labeled_array, num_features = scipy.ndimage.label(image)
    sizes = scipy.ndimage.sum(image, labeled_array, range(num_features + 1))
    mask_sizes = sizes == 1
    remove_pixels = mask_sizes[labeled_array]
    image[remove_pixels] = 0
    return image

square = np.zeros((32, 32))
square[10:-10, 10:-10] = np.random.randint(1, 255, size=(12, 12))
np.random.seed(12)
x, y = (32 * np.random.random((2, 20))).astype(int)
square[x, y] = np.random.randint(1, 255, size=(20,))

square = remove_isolated_cells(square)
print(square)
