# Binary Search Algorithms work only with sorted arrays.
def binarysearch(value, array):
	low = 0
	high = len(array)-1
	while low <= high:
		mid = (low + high)//2
		if value == array[mid]:
			return True
		elif value < array[mid]:
			high = mid - 1
		elif value > array[mid]:
			low = mid + 1
	return False

#implementation
arr1 = [1, 2, 3, 4, 5]

print(binarysearch(3, arr1))
print(binarysearch(5, arr1))
print(binarysearch(10, arr1))
print(binarysearch(7, arr1))
print(binarysearch(9, arr1))
print(binarysearch(1, arr1))
