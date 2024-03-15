def solve_for_a(x, b):
    def eqn(a):
        return x + 2*a - b**2
    return fsolve(eqn, x0=0.5)

result = np.array([solve_for_a(x, b) for x, b in zip(xdata, bdata)])
