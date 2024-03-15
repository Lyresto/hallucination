import scipy.integrate

def f(c, low, high):
    results = []
    for i in range(len(c)):
        eqn = lambda x: 2 * c[i] * x
        result, error = scipy.integrate.quad(eqn, low, high)
        results.append(result)
    return results

c = [1, 2, 3, 4, 5]
low = 0
high = 1
solution = f(c, low, high)
print(solution)