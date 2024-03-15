plt.scatter(b, a)
for i, txt in enumerate(c):
    plt.annotate(txt, (b[i], a[i]))
plt.xlabel('b')
plt.ylabel('a')
plt.title('Scatter Plot of a over b')
plt.show()
