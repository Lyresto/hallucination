def fourier(x, *coefficients):
    result = 0
    for i, coeff in enumerate(coefficients):
        result += coeff * np.cos((i+1) * np.pi / tau * x)
    return result

initial_guess = [1] * degree
popt, pcov = curve_fit(fourier, z, Ua, p0=initial_guess)
