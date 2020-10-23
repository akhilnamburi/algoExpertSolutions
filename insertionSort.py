'''
TC: O(n**2)
SC:O(1)
'''
def insertionSort(array):
    for i in range(1, len(array)):
		currentValue=array[i]
		while i> 0 and array[i-1]>currentValue:
			array[i] = array[i-1]
			i -=1
		array[i] = currentValue
	return array