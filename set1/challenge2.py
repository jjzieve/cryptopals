#!/usr/bin/python

def xor_hex(str_hex1,str_hex2):
	return int(str_hex1,16) ^ int(str_hex2,16)

if __name__=="__main__":
	str_hex1 = raw_input("first xor value (hex): ")
	str_hex2 = raw_input("second xor value (hex): ")
	""" Apparently, format() loops through each bit? """
	print "xor value: {:x}".format(xor_hex(str_hex1,str_hex2))
