# solution 1 with 
# TC: O(n**2)
# SC: O(1) 
def twoNumberSum(array, targetSum):
	
	for idx1 in range(len(array)):
		for idx2 in range(idx1, len(array)):
			if idx1 !=idx2 and array[idx1]+array[idx2] == targetSum:
				return [array[idx1],array[idx2]]
	return []

'''
solution2
TC : O(nlogn)
SC: O(1)
'''
def twoNumberSum(array, targetSum):
    array.sort()
	left=0
	right=len(array)-1
	while left< right:
		currentSum = array[left]+array[right]
		if currentSum == targetSum:
			return [array[left],array[right]]
		elif currentSum< targetSum:
			left+=1
		elif currentSum>targetSum:
			right-=1
	return []

