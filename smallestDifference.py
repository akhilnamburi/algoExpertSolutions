'''
TC: O(nlogn)+O(mlogm)
SC: O(1)
'''

def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	idx1=0
	idx2=0
	smallest=float("inf")
	current = float("inf")
	smallestPair=[]
	while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
		num1 = arrayOne[idx1]
		num2 = arrayTwo[idx2]
		if num1<num2:
			current = num2-num1
			idx1+=1
		elif num2<num1:
			current = num1-num2
			idx2+=1
		else:
			return [num1,num2]
		if smallest>current:
			smallest = current
			smallestPair=[num1, num2]
	return smallestPair
	