result = []
rows, cols = a.shape
for i in range(rows):
    for j in range(cols):
        window = a[max(0, i-size[0]//2):min(rows, i+size[0]//2+1), max(0, j-size[1]//2):min(cols, j+size[1]//2+1)]
        result.append(window)
