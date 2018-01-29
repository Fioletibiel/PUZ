import numpy as np

pole = [[0 for x in range(100)] for y in range(100)]
for x in range(100):
    for y in range(100):
        pole[x][y] = np.random.randint(0, 2)
print(np.matrix(pole))