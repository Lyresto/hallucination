B = pd.Series(index=A.index)
B[0] = a * A[0]
for t in range(1, len(A)):
    B[t] = a * A[t] + b * B[t-1]
