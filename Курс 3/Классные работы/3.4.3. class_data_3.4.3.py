import numpy as np
filename = input()
matrix = np.genfromtxt(filename, delimiter=' ', dtype=np.float16)
result = np.sum(matrix[:, 3])
print(result)
