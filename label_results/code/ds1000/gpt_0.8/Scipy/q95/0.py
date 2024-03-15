def solve_for_a(x, b):
    def eqn(a):
        return x + 2*a - b**2

    a_guess = 0.5
    solution = fsolve(eqn, a_guess)
    return solution

result = [solve_for_a(x, b) for x, b in zip(xdata, bdata)]
