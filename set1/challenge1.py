#!/usr/bin/python
import base64 # hehe python

"""
now... from what I understand under the hood it just has a dictionary mapping 
base64 values (i.e. "T":01001101) so I would've just done that anyways? 
"""
def hex_to_64(str_hex):
	return base64.b64encode(str_hex.decode("hex"))

if __name__=="__main__":
	print "base64: "+hex_to_64(raw_input("hex: "))
