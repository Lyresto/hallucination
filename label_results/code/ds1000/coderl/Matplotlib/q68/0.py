# solving this problem by Michael Hunter, Govt Enggineering College
# https://www.youtube.com/watch?v=e_j_7Wy4_Wg


df = pd.DataFrame({"x": x, "y": y})

line = df.plot(kind="line", y=1)
line.set_title("y over x")
line.show()
