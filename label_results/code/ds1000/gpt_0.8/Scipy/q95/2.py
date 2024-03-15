def eqn(a, x, b):
    return x + 2*a - b**2

result = []

for i in range(len(xdata)):
    root = fsolve(eqn, x0=0.5, args=(xdata[i], bdata[i]))
    result.append(root)

result = np.array(result)
print(result)
END SOLUTION
