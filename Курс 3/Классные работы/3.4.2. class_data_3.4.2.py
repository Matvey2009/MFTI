import numpy as np
def no_negative(arr):
	new_arr = np.copy(arr)
	new_arr[new_arr < 0] = 0
	return new_arr
