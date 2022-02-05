from convert_number_system import *
from rearrange_bits import *
from tables import *

'''
DES encryption algorithm with xor and hamming helper function.
'''
# calculating xor of two strings of binary number a and b
def xor(a, b):
	ans = ""
	for i in range(len(a)):
		if a[i] == b[i]:
			ans = ans + "0"
		else:
			ans = ans + "1"
	return ans

def hamming(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def encrypt(pt, rkb, rk, delta_ct, ct_first, is_first):
	pt = hex2bin(pt)
	
	# Initial Permutation
	pt = permute(pt, initial_perm, 64)
	
	# Splitting
	left = pt[0:32]
	right = pt[32:64]

	delta_ct_of_each_pk = []

	for i in range(0, 16):
		# Expansion D-box: Expanding the 32 bits data into 48 bits
		right_expanded = permute(right, exp_d, 48)
		
		# XOR RoundKey[i] and right_expanded
		xor_x = xor(right_expanded, rkb[i])

		# S-boxex: substituting the value from s-box table by calculating row and column
		sbox_str = ""
		for j in range(0, 8):
			row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
			col = bin2dec(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
			val = sbox[j][row][col]
			sbox_str = sbox_str + dec2bin(val)
			
		# Straight D-box: After substituting rearranging the bits
		sbox_str = permute(sbox_str, per, 32)
		
		# XOR left and sbox_str
		result = xor(left, sbox_str)
		left = result
		
		# Swapper
		if(i != 15):
			left, right = right, left
		# print("Round ", i + 1, " ", bin2hex(left), " ", bin2hex(right), " ", rk[i])
		ct_of_each_round = bin2hex(left) + bin2hex(right)

		if(is_first):
			ct_first.append(ct_of_each_round)

		else:
			delta_ct_of_each_pk.append(hamming(hex2bin(ct_first[i]), hex2bin(ct_of_each_round)))

	if(is_first == False):
		delta_ct.append(delta_ct_of_each_pk)

	# Combination
	combine = left + right
	
	# Final permutation: final rearranging of bits to get cipher text
	cipher_text = permute(combine, final_perm, 64)
	return