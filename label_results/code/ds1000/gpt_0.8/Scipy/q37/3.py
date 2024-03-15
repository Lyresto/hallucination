def fourier(x, *params):
    result = 0
    for i in range(1, len(params)+1):
        result += params[i-1] * np.cos(i * np.pi / tau * x)
    return result

p0 = [1] * degree  # initial guess for parameters
popt, pcov = curve_fit(fourier, z, Ua, p0=p0)
END SOLUTION
