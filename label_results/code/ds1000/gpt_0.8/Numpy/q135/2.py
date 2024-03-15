import numpy as np

def convert_to_binary(num, m):
    # Convert the number to binary and remove the '0b' prefix
    binary = bin(num)[2:]
    # Pad the binary string with leading zeros to match the desired length
    padded_binary = binary.zfill(m)
    # Convert the padded binary string to a numpy array of integers
    binary_array = np.array(list(padded_binary), dtype=int)
    
    return binary_array

# Test the function
a = np.array([1, 2, 3, 4, 5])
m = 6
result = np.zeros((a.shape[0], m))
for i in range(a.shape[0]):
    result[i] = convert_to_binary(a[i], m)
result