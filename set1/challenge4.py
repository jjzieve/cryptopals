#!/usr/bin/python
import challenge3
import sys
def single_byte_decode_file(f):
	results_scores = {}
	results_meta = {}
	for i,line in enumerate(open(f).read().strip().split("\n")):
		result = challenge3.single_byte_decode(line)
		results_scores[result[1]] = challenge3.score(result[1])
		results_meta[result[1]] = [result[0],i] 
	answer = max(results_scores, key=results_scores.get)
	return results_meta[answer]+[answer]

if __name__=="__main__":
	result = single_byte_decode_file(sys.argv[1])
	print "Key: "+result[0]+"\n"+"Line number: "+str(result[1])+"\n"+"Message: "+result[2]
