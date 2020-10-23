'''
TC: O(n)
SC:O(1)
'''

def isMonotonic(array):
	if len(array)>2:
		pattern = ""
		if array[0]>array[-1]:
			pattern = "decrease"
		else:
			pattern = "increase"	

		for idx in range(len(array)-1):
			order=""
			if array[idx] > array[idx+1]:
				order = "decrease"
			elif array[idx]<array[idx+1]:
				order = "increase"
			else:
				order = pattern

			if pattern != order:
				return False
		return True
	else:
		return True



'''
Solution 2
'''

def isMonotonic(array):
    decreasing=True
	increasing=True
	for i in range(1,len(array)):
		if array[i]<array[i-1]:
			decreasing = False
		if array[i]>array[i-1]:
			increasing = False
	return increasing or decreasing