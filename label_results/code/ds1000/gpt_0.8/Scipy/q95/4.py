result = []
for i in range(len(xdata)):
    sol = fsolve(lambda a: eqn(xdata[i], a, bdata[i]), x0=0.5)
    result.append(sol[0])
result = np.array(result)
