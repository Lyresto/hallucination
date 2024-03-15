import numpy as np

def f(X):
    result = []
    for row in X:
        for element in row:
            result.append(element)
    return result

# Example usage
example_X = np.random.randint(2, 10, (5, 6))
result = f(example_X)
print(result)