#TC: O(log(n))
#SC: O(log(n))

def shiftedBinarySearch(array, target):
	start, end = 0, len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] >= array[start]:
            if target >= array[start] and target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= array[end] and target > array[mid]: 
                start = mid + 1
            else:
                end = mid - 1
    return -1