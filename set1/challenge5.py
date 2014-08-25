#!/usr/bin/python

def repeating_key_xor_encrypt(key,message):
	key_bin = map(ord,key)
	index = 0
	encrypted_message_list = []
	for char in message:
		if index == len(key_bin):
			index = 0 #reset index when its run its course
		encrypted_message_list.append(ord(char) ^ key_bin[index])
		index += 1
	print "".join(map(chr,encrypted_message_list)).encode("hex")

if __name__=="__main__":
	repeating_key_xor_encrypt("ICE","Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
	# message = raw_input("Enter message: \n")
	# key = raw_input("Enter key: \n")
	# repeating_key_xor_encrypt(key,message)

	