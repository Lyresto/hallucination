plt.scatter(a, b)
for i, txt in enumerate(c):
    plt.annotate(txt, (a[i], b[i]))
plt.xlabel('a')
plt.ylabel('b')
plt.title('Scatter plot of a over b')
plt.show()
