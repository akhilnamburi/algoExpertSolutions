'''
TC:O(nlog(n))
SC: O(log(n))
'''

def quickSort(array):
	partition(array,0,len(array)-1)
	return array

def partition(array,start,end):
	if start>=end:
		return
	pivot = start
	left = start+1
	right = end
	while right>=left:
		if array[left]>array[pivot] and array[right]<array[pivot]:
			array[left],array[right] = array[right],array[left]
		if array[left]<=array[pivot]:
			left+=1
		if array[right]>=array[pivot]:
			right-=1
	array[pivot],array[right] = array[right], array[pivot]
	leftSubArraySmaller = right-1-start<end-(right+1)
	if leftSubArraySmaller:
		partition(array,start,right-1)
		partition(array,right+1,end)
	else:
		partition(array,right+1,end)
		partition(array,start,right-1)
		


