x_new = np.linspace(0, 2, 4)
y_new = np.linspace(0, 2, 4)
result = intp.interp2d(x_new, y_new, a, kind='linear')
