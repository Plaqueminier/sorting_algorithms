#!/usr/bin/python3.6

from create import createRandomArr
import time

def mergeSort(arr):
	n = len(arr)
	width = 1
	while (width < n):
		tmpArr = []
		i = 0
		while (i < n):
			left = min(i + width, n)
			mid = min(i + width, n)
			right = min(i + 2 * width, n)
			tmpArr += (mergePair(arr[i:left], arr[mid:right]))
			i = i + 2 * width
		arr = tmpArr
		width *= 2
	return (arr)

def mergePair(arrL, arrR):
	i = 0
	j = 0
	newArr = []
	size1 = len(arrL)
	size2 = len(arrR)
	append = newArr.append
	while (i < size1 and j < size2):
		if (arrL[i] <= arrR[j]):
			append(arrL[i])
			i += 1
		else:
			append(arrR[j])
			j += 1
	while (i < size1):
		append(arrL[i])
		i += 1
	while (j < size2):
		append(arrR[j])
		j += 1
	return (newArr)

if __name__ == "__main__":
	size = 100000
	arr = createRandomArr(size)
	startTime = time.time()
	mergeSort(arr)
	print ("Bottom Up Merge Sort Time Taken :", (time.time() - startTime), "s for", size, "numbers")