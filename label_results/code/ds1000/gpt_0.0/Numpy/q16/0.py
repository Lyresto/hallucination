result = np.zeros_like(a)
for i, s in enumerate(shift):
    if s > 0:
        result[i, s:] = a[i, :-s]
    elif s < 0:
        result[i, :s] = a[i, -s:]
    else:
        result[i] = a[i]
result = np.where(result == 0, np.nan, result)
