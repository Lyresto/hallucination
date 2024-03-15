def fourier(x, *coefficients):
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * np.cos((i+1) * np.pi / tau * x)
    return result

popt, pcov = curve_fit(fourier, z, Ua, p0=[1] * degree)
