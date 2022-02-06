import numpy as np
import matplotlib.pyplot as plt
from tables import *
from convert_number_system import *
from rearrange_bits import *
from des_encryption import *

'''
Main function demonstrating Avalanche effect in DES algorithm across the 16 rounds.
'''

def key_preparer(key, keyp, rkb, rk):
	"""
	Generates and stores the keys for all the 16 rounds of DES in rkb and rk lists.
	"""

	# Key generation
    # --hex to binary
	key = hex2bin(key)

    # getting 56 bit key from 64 bit using the parity bits
	key = permute(key, keyp, 56)

    # Splitting
	left = key[0:28] # rkb for RoundKeys in binary
	right = key[28:56] # rk for RoundKeys in hexadecimal

	for i in range(0, 16):
        # Shifting the bits by nth shifts by checking from shift table
		left = shift_left(left, shift_table[i])
		right = shift_left(right, shift_table[i])
        
        # Combination of left and right string
		combine_str = left + right
        
        # Compression of key from 56 to 48 bits
		round_key = permute(combine_str, key_comp, 48)

		rkb.append(round_key)
		rk.append(bin2hex(round_key))	

def get_box_plots(delta_ct, save_plot_path):
	"""
	Generates and stores the box plots of the delta_ct results of our experiments.
	"""

	plt.boxplot(np.array(delta_ct).T.tolist())
	plt.savefig(save_plot_path)
	plt.show()

def fill_delta_ct(pt, key, delta_ct, ct_first, is_first):
	"""
	Initiates the DES encryption and obtains the delta_ct list.
	"""

	rkb = []
	rk = []

	key_preparer(key, keyp, rkb, rk)
	encrypt(pt, rkb, rk, delta_ct, ct_first, is_first)	
	return rkb, rk

def get_delta_ct(pt, key, save_plot_path):
	"""
	Calls all the helper functions to complete the experiments end to end.
	"""

	delta_ct = []
	ct_first = []	

	rkb, rk = fill_delta_ct(pt[0], key, delta_ct, ct_first, True)

	for i in range(1, 6):
		encrypt(pt[i], rkb, rk, delta_ct, ct_first, False)
		print(delta_ct[i-1])
 
	get_box_plots(delta_ct, save_plot_path)

def main():
	"""
	All the avalanche effect experiments are initiated here.
	"""

	#####################################################################################################################################################
	print("Case 1: Five different plain texts at hemmming distance of 1 with a plain text.")
	'''
	Case 1: Five different plain texts at hemmming distance of 1 with a plain text.
	'''
	pt = ["123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536"] #"123456ABCD132536"
	key = "AABB09182736CCDD"

	get_delta_ct(pt, key, 'plots/case1.png')

	#####################################################################################################################################################
	print("Case 2: Five different plain texts at different hemmming distances with a plain text.")
	'''
	Case 2: Five different plain texts at different hemmming distances with a plain text.
	'''
	pt = ["123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536"] #"123456ABCD132536"
	key = "AABB09182736CCDD"

	get_delta_ct(pt, key, 'plots/case2.png')

	#####################################################################################################################################################
	print("Case 3: Five different secret keys at hemmming distance of 1 with a secret key.")
	'''
	Case 3: Five different secret keys at hemmming distance of 1 with a secret key.
	'''
	pt = "123456ABCD132536"
	key = ["AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD"] #"AABB09182736CCDD"
	delta_ct = []
	ct_first = []
	
	fill_delta_ct(pt, key[0], delta_ct, ct_first, True)

	for j in range(1, 6):
		fill_delta_ct(pt, key[j], delta_ct, ct_first, False)
		print(delta_ct[j-1])	

	get_box_plots(delta_ct, 'plots/case3.png')
	
	#####################################################################################################################################################

main()
print("Experiments successful")
