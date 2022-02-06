'''
Functions for the manipulation of the arrangement of the bits.
'''

def permute(k, arr, n):
	"""
	Permute function to rearrange the bits.
	"""
	permutation = ""
	for i in range(0, n):
		permutation = permutation + k[arr[i] - 1]
	return permutation

def shift_left(k, nth_shifts):
	"""
	Shifting the bits towards left by nth shifts.
	"""
	s = ""
	for i in range(nth_shifts):
		for j in range(1,len(k)):
			s = s + k[j]
		s = s + k[0]
		k = s
		s = ""
	return k