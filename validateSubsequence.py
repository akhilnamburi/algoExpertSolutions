'''
TC: O(n)
SC: O(1)
'''

def isValidSubsequence(array, sequence):
	idx = 0
	for value in array:
		if idx == len(sequence):
			break
		if sequence[idx] == value:
			idx+=1
	if len(sequence) == idx:
		return True
	else:
		return False