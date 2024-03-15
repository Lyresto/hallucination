import numpy as np
probabilit = [0.333, 0.333, 0.333]
lista_elegir = [(3, 3), (3, 4), (3, 5)]
samples = 1000
np.random.choice(lista_elegir, samples, probabilit)
