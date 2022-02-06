from convert_number_system import *
from rearrange_bits import *
from tables import *

'''
DES encryption algorithm with helper functions.
'''

# calculating xor of two strings of binary number a and b
def xor(a, b):
	"""
	Calculate the xor of two strings of binary number a and b.
	"""

	ans = ""
	for i in range(len(a)):
		if a[i] == b[i]:
			ans = ans + "0"
		else:
			ans = ans + "1"
	return ans

def hamming(s1, s2):
    """
	Calculate the Hamming distance between two bit strings
	"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def phase1(pt, initial_perm, no_of_bits_in_binary):
	"""
	Initial permutation phase of the DES algorithm where the bits are rearranged.
	"""

	pt = hex2bin(pt)
	
	# Initial Permutation
	pt = permute(pt, initial_perm, no_of_bits_in_binary)
	return pt

def phase2(pt, delta_ct_of_each_pk, rkb, rk, delta_ct, ct_first, is_first):
	"""
	The phase where the 16 rounds are performed in the DES algorithm.
	Here:
		Li = Ri-1 and
		Ri = XOR(Li-1, F(Ri-1, ki))
	"""

	# Splitting
	left = pt[0:32]
	right = pt[32:64]

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

	return left, right

def phase3(left, right, no_of_bits_in_binary):
	"""
	This is phase 3 of the DES algorithm where final permutation is performed to get the cipher text in the DES algorithm.
	"""

	# Combination
	combine = left + right
	
	# Final permutation: final rearranging of bits to get cipher text
	cipher_text = permute(combine, final_perm, no_of_bits_in_binary)

def encrypt(pt, rkb, rk, delta_ct, ct_first, is_first):
	"""
	DES encryption function which calles the DES phase functions to get the final cipher text.
	"""

	no_of_bits_in_binary = 64

	pt = phase1(pt, initial_perm, no_of_bits_in_binary)

	delta_ct_of_each_pk = []
	left, right = phase2(pt, delta_ct_of_each_pk, rkb, rk, delta_ct, ct_first, is_first)

	cipher_text = phase3(left, right, no_of_bits_in_binary)
	return