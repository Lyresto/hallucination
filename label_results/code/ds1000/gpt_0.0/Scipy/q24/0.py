# Define the cost function to minimize
def cost_function(assignment, points1, points2):
    total_distance = 0
    for i in range(len(assignment)):
        total_distance += scipy.spatial.distance.cityblock(points1[i], points2[assignment[i]])
    return total_distance

# Define the constraints for the optimization problem
constraints = []
for i in range(N):
    constraints.append({'type': 'eq', 'fun': lambda x, i=i: np.sum(x == i) - 1})
for j in range(N):
    constraints.append({'type': 'eq', 'fun': lambda x, j=j: np.sum(x == j) - 1})

# Solve the optimization problem
initial_guess = np.arange(N)
result = scipy.optimize.minimize(cost_function, initial_guess, args=(points1, points2), method='SLSQP', constraints=constraints)
result = result.x.astype(int)
