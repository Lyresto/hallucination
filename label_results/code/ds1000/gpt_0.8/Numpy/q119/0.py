import numpy as np
probabilit = [0.333, 0.333, 0.333]
lista_elegir = [(3, 3), (3, 4), (3, 5)]
samples = 1000

# Convert the list of tuples into a numpy array
array_elegir = np.array(lista_elegir)

# Use the numpy.random.choice function with the array_elegir and probabilit
result = np.random.choice(array_elegir, size=samples, p=probabilit)
END SOLUTION

print(result)