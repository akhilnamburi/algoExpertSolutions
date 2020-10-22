def moveElementToEnd(array, toMove):
	for i in array:
		if i==toMove:
			array.remove(i)
			array.append(i)
			print(array)
	return array