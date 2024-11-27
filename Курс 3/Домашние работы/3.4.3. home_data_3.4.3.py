import numpy as np
def cross_max(matrix):
	max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
	modified_matrix = np.copy(matrix)
	modified_matrix[max_index[0], :] = np.max(matrix)
	modified_matrix[:, max_index[1]] = np.max(matrix)
	return modified_matrix
