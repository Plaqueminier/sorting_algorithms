#!/usr/bin/python3.6

from create import createRandomArr
import time

def quickSort(arr, l, r):
	if l < r:
		pi = partition(arr, l, r)
		quickSort(arr, l, pi - 1)
		quickSort(arr, pi, r)

def partition(arr, l, r):
	p = arr[l]
	i = l+1
	for j in range(l+1, r):
		if (arr[j] <= p):
			arr[j], arr[i] = arr[i], arr[j]
			i += 1

	arr[l], arr[i-1] = arr[i-1], arr[l]
	return (i)

if __name__ == "__main__":
	size = 100000
	arr = createRandomArr(size)
	startTime = time.time()
	quickSort(arr, 0, size)
	print ("Quick Sort Time Taken :", (time.time() - startTime), "s for", size, "numbers")