def linearsearch(value, array):
	for item in array:
		if item == value:
			return True
	return False


#implementation
arr1 = ["hello", 1, "world", 2]

print(linearsearch("hello", arr1))
print(linearsearch(5, arr1))
print(linearsearch("world", arr1))
print(linearsearch(2, arr1))
print(linearsearch("mishra", arr1))
print(linearsearch(0, arr1))