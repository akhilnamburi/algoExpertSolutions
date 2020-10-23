'''
TC: O(n**2)
SC: O(1)
'''

def selectionSort(array):
	for i in range(len(array)-1):
		smallestIdx = i
		for j in range(i+1, len(array)):
			if array[j]<array[smallestIdx]:
				smallestIdx = j
		array[i], array[smallestIdx] = array[smallestIdx], array[i]
	return array