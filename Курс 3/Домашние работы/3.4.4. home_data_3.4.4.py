import numpy as np
def is_orth(vect1, vect2):
	if vect1[0]*vect2[0]+vect1[1]*vect2[1]+vect1[2]*vect2[2] == 0:
		return True
	else:
		return False
