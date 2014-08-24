#!/usr/bin/python
from collections import Counter

def most_common(l):
	return Counter(l).most_common(1)[0][0]

# find the most common int, xor against char 
def brute_force_decrypt(char,string):
	encoded_ascii_codes = map(ord,string.decode("hex")) #decode hex and map to ascii ints
	most_common_code = most_common(encoded_ascii_codes) #find most common code/int/letter
	key = ord(char) ^ most_common_code #xor against char which will be e,t,a,o,etc... for the key
	#build the (potentially) decrypted codes by xor'ing against key
	decrypted_ascii_codes = []
	for code in encoded_ascii_codes:
		decrypted_ascii_codes.append(key ^ code)
	#log each key and the (potentially) decypted message after mapping them back to chars and joining them into a string
	return [chr(key),"".join(map(chr,decrypted_ascii_codes))]

def score(decoded_message):#kinda crude but should do the job
	etaoin_shrdlu_dict = {"e":13,"t":12,"a":11,"o":10,"i":9,"n":8," ":7,"s":6,"h":5,"r":4,"d":3,"l":2,"u":1} 
	score = 0
	for char in decoded_message:
		if char in etaoin_shrdlu_dict:
			score += etaoin_shrdlu_dict[char]
	return score

def single_byte_decode(encoded_message):
	#check for all the most frequent letters in english (could just brute force with ascii?)
	etaoin_shrdlu = ["e","t","a","o","i","n"," ","s","h","r","d","l","u"] 
	results = {}
	results_meta = {} #to store the key
	for char in etaoin_shrdlu:
		result = brute_force_decrypt(char,encoded_message)
		results_meta[result[1]] = result[0]
		results[result[1]] = score(result[1])
	answer = max(results, key=results.get) # get the highest scoring decrypted message, it should be the original message
	key = results_meta[answer] #get the culprit key
	return [key,answer] #return both

if __name__=="__main__":
	encoded_message = raw_input("Enter single-byte xor cipher: ")
	results = single_byte_decode(encoded_message)
	print "Key: "+results[0]+"\nMessage: "+results[1]

