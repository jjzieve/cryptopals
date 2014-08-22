#!/usr/bin/python

from challenge2 import xor_hex
import string

def single_byte_decode(encoded_message):
	scores = {"E":13,"T":12,"A":11,"O":10,"I":9,"N":8," ":7,"S":6,"H":5,"R":4,"D":3,"L":2,"U":1}
	#brute-force decrypt and return string with highest ETAOIN SHRDLU score?
	for char in list(string.ascii_letters):
		print "{:x}".format(xor_hex(encoded_message,char.encode("hex")))

if __name__=="__main__":
	print "Decoded message: "+single_byte_decode(raw_input("Enter single-byte xor cipher: "));
