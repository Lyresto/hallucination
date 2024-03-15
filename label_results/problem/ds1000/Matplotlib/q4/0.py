y = np.random.rand(10, 4)
line_styles = ['-', '--', '-.', ':']
for i in range(4):
    plt.plot(x, y[:, i], linestyle=line_styles[i])
