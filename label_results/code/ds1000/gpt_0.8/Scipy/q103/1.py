def find_extrema(arr, n):
    extrema_indices = []
    
    for i in range(len(arr)):
        # Check if current element is less than or equal to the neighbouring elements
        if i >= n and i < len(arr) - n and arr[i] <= arr[i-n:i+n+1].max():
            extrema_indices.append(i)
    
    return extrema_indices

result = find_extrema(arr, n)
