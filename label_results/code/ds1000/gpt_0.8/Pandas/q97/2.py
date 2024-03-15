df = df[(df.filter(like='Value').abs() < 1).all(axis=1)]
