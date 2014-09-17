#!/usr/bin/python
import base64
import sys

#xnor should test bit equality, so just count 1's from a xor bitwise operation?
#too lazy, char comparison ftw!
def bitwise_hamming_distance(str1,str2): #assuming equal length?
	assert(len(str1) == len(str2)) 
	hamming_distance = 0
	for char1,char2 in zip(str1,str2):
		bit_list1 = bin(ord(char1))[2:].zfill(8)#the [2:] takes off "b0" which signifies a binary string, the zfill makes sure leading zeroes aren't chopped off
		bit_list2 = bin(ord(char2))[2:].zfill(8)
		hamming_distance += sum(bit1 != bit2 for bit1,bit2 in zip(bit_list1,bit_list2))
	return hamming_distance

#fastest way but tricky with python leaving off "extraneous" leading zeroes, TODO: implement!
def bitstring_hamming(x,y):
    count,z = 0,x^y
    while z:
        count += 1
        z &= z-1 # magic!
    return count

def break_repeating_key_xor(estimate_key_size_range,file_handle):
	lines = map(base64.b64decode,open(file_handle).read().strip().split("\n"))
	print estimate_key_size_range[1]
	print len(lines[0]+lines[1])
	# key_size = determine_key_size(estimate_key_size_range)
	# for i,line in enumerate(open(file_handle).read().strip().split("\n")):
	# 	print base64.b64decode(line)

def transpose(string):
	return "TODO"

def find_keysize(range,string):
	potential_keysizes = []
	for i in xrange(range[0],range[1]):
		potential_keysizes.append(bitwise_hamming_distance(string[0:i],string[i+1:(2*i)+1])/i)
	return sorted(potential_keysizes,reverse=True)[0:2]

def split_into_blocks(cipher,keysize):
	blocks = []
	block = ""
	#transpose inline?
	for i,byte in enumerate(cipher):
		if i==(keysize-1):
			blocks.append(block)
		else:
			block+=byte
	return blocks

if __name__=="__main__":
	#print bitwise_hamming_distance("this is a test","wokka wokka!!!")
	print break_repeating_key_xor([2,41],sys.argv[1])


	