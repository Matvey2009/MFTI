import numpy as np
n = int(input())
print(np.array([i for i in range(1, n) if i % 7 == 0 and i % 3 != 0]))
