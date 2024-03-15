def fourier(x, *coeffs):
    result = 0
    for i in range(1, len(coeffs)+1):
        result += coeffs[i-1] * np.cos(i * np.pi / tau * x)
    return result

popt, pcov = curve_fit(fourier, z, Ua, p0=[1]*(degree))

# To plot only the first harmonic
popt1 = [popt[0]]
pcov1 = [[pcov[0][0]]]

x_vals = np.linspace(min(z), max(z), 100)
y_vals = fourier(x_vals, *popt1)
plt.plot(x_vals, y_vals, label='First Harmonic')

# To plot all harmonics
y_vals = fourier(x_vals, *popt)
plt.plot(x_vals, y_vals, label='All Harmonics')

plt.plot(z, Ua, 'ro', label='Data')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
