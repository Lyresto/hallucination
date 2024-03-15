def fourier(x, *a):
    result = 0
    for i in range(1, degree+1):
        result += a[i-1] * np.cos(i * np.pi / tau * x)
    return result

popt, pcov = curve_fit(fourier, z, Ua, p0=[1]*degree)
