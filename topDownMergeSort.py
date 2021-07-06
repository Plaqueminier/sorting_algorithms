#!/usr/bin/python3.6

from create import createRandomArr
import time

def mergeSort(arr):
	arr1 = []
	arr2 = []
	mid = len(arr) // 2 if len(arr) // 2 > 0 else 1

	arr1 = arr[:mid]
	arr2 = arr[mid:]
	return (mergeLists(arr1, arr2))

def mergeLists(arr1, arr2):
	if (len(arr1) == 1 and len(arr2) == 1):
		return ([arr1[0], arr2[0]] if arr1[0] <= arr2[0] else [arr2[0], arr1[0]])
	i = 0
	j = 0
	auxArr1 = mergeSort(arr1) if len(arr1) > 1 else arr1
	auxArr2 = mergeSort(arr2) if len(arr2) > 1 else arr2
	auxArr = []
	while (i < len(auxArr1) or j < len(auxArr2)):
		if (j >= len(auxArr2) or (i < len(auxArr1) and auxArr1[i] <= auxArr2[j])):
			auxArr.append(auxArr1[i])
			i += 1
		else:
			auxArr.append(auxArr2[j])
			j += 1
	return (auxArr)

if __name__ == "__main__":
	size = 100000
	arr = createRandomArr(size)
	startTime = time.time()
	mergeSort(arr)
	print ("Top Down Merge Sort Time Taken :", (time.time() - startTime), "s for", size, "numbers")