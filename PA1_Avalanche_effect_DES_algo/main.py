import numpy as np
import matplotlib.pyplot as plt
from tables import *
from convert_number_system import *
from rearrange_bits import *
from des_encryption import *

'''
Main function demonstrating Avalanche effect in DES algorithm across the 16 rounds.
'''
def main():

	#####################################################################################################################################################
	#####################################################################################################################################################
	#####################################################################################################################################################
	print("Case 1: Five different plain texts at hemmming distance of 1 with a plain text.")
	'''
	Case 1: Five different plain texts at hemmming distance of 1 with a plain text.
	'''
	pt = ["123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536"] #"123456ABCD132536"
	delta_ct = []
	ct_first = []
	key = "AABB09182736CCDD"

	# Key generation
    # --hex to binary
	key = hex2bin(key)

    # getting 56 bit key from 64 bit using the parity bits
	key = permute(key, keyp, 56)

    # Splitting
	left = key[0:28] # rkb for RoundKeys in binary
	right = key[28:56] # rk for RoundKeys in hexadecimal

	rkb = []
	rk = []
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

	encrypt(pt[0], rkb, rk, delta_ct, ct_first, True)

	for i in range(1, 6):
		encrypt(pt[i], rkb, rk, delta_ct, ct_first, False)
		print(delta_ct[i-1])

	plt.boxplot(np.array(delta_ct).T.tolist())
	plt.savefig('case1.png')
	plt.show() 

	#####################################################################################################################################################
	#####################################################################################################################################################
	#####################################################################################################################################################
	print("Case 2: Five different plain texts at different hemmming distances with a plain text.")
	'''
	Case 2: Five different plain texts at different hemmming distances with a plain text.
	'''

	pt = ["123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536", "123456ABCD132536"] #"123456ABCD132536"
	delta_ct = []
	ct_first = []
	key = "AABB09182736CCDD"

	# Key generation
    # --hex to binary
	key = hex2bin(key)

    # getting 56 bit key from 64 bit using the parity bits
	key = permute(key, keyp, 56)

    # Splitting
	left = key[0:28] # rkb for RoundKeys in binary
	right = key[28:56] # rk for RoundKeys in hexadecimal

	rkb = []
	rk = []
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

	encrypt(pt[0], rkb, rk, delta_ct, ct_first, True)

	for i in range(1, 6):
		encrypt(pt[i], rkb, rk, delta_ct, ct_first, False)
		print(delta_ct[i-1])

	plt.boxplot(np.array(delta_ct).T.tolist())
	plt.savefig('case2.png')
	plt.show() 

	#####################################################################################################################################################
	#####################################################################################################################################################
	#####################################################################################################################################################
	print("Case 3: Five different secret keys at hemmming distance of 1 with a secret key.")
	'''
	Case 3: Five different secret keys at hemmming distance of 1 with a secret key.
	'''
	pt = "123456ABCD132536"
	key = ["AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD", "AABB09182736CCDD"] #"AABB09182736CCDD"
	delta_ct = []
	ct_first = []

	# Key generation
    # --hex to binary
	key[0] = hex2bin(key[0])

	# getting 56 bit key from 64 bit using the parity bits
	key[0] = permute(key[0], keyp, 56)

    # Splitting
	left = key[0][0:28] # rkb for RoundKeys in binary
	right = key[0][28:56] # rk for RoundKeys in hexadecimal

	rkb = []
	rk = []
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

	encrypt(pt, rkb, rk, delta_ct, ct_first, True)

	for j in range(1, 6):
		key[j] = hex2bin(key[j])

    	# getting 56 bit key from 64 bit using the parity bits
		key[j] = permute(key[j], keyp, 56)

		# Splitting
		left = key[j][0:28] # rkb for RoundKeys in binary
		right = key[j][28:56] # rk for RoundKeys in hexadecimal

		rkb = []
		rk = []
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

		encrypt(pt, rkb, rk, delta_ct, ct_first, False)
		print(delta_ct[j-1])	

	plt.boxplot(np.array(delta_ct).T.tolist())
	plt.savefig('case3.png')
	plt.show() 
	#####################################################################################################################################################
	#####################################################################################################################################################
	#####################################################################################################################################################

main()
