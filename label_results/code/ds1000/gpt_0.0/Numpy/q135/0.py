def int_to_bin_array(num, m):
    if num < 0:
        num = 2**m + num
    bin_str = bin(num)[2:]
    bin_arr = np.zeros(m, dtype=int)
    for i in range(len(bin_str)):
        bin_arr[m-len(bin_str)+i] = int(bin_str[i])
    return bin_arr

result = np.zeros((len(a), m), dtype=int)
for i in range(len(a)):
    result[i] = int_to_bin_array(a[i], m)
