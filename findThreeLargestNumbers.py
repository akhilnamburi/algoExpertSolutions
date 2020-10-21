'''
TC: O(n)
SC: O(1)
'''

def findThreeLargestNumbers(array):
    threeLargest=[None,None,None]
	for num in array:
		if threeLargest[2] is None or num > threeLargest[2]:
			for i in range(2+1):
				if i== 2:
					array[i] = num
				else:
					array[i] = array[i+1]
		elif threeLargest[1] is None or num > threeLargest[1]:
			for i in range(1+1):
				if i== 1:
					array[i] = num
				else:
					array[i] = array[i+1]
		elif threeLargest[0] is None or num > threeLargest[0]:
			for i in range(0+1):
				if i== 0:
					array[i] = num
				else:
					array[i] = array[i+1]
	return threeLargest

