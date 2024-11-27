filename = input()
import numpy as np
with open(filename, 'r') as file:
	numbers = np.array([int(num) for num in file.read().split()], dtype=np.int16)
nonzero_indices = np.nonzero(numbers)[0]
print(nonzero_indices)
