#!/usr/bin/python3.6

from create import createRandomArr
import time

def tQuickSort(arr, l, r):
	if l < r:
		(i, j) = tPartition(arr, l, r)
		tQuickSort(arr, l, i - 1)
		tQuickSort(arr, j, r)

def tPartition(arr, l, r):
	p = arr[l]
	i = l+1
	j = l+1
	for k in range(l+1, r):
		if (arr[k] < p):
			arr[k], arr[i] = arr[i], arr[k]
			if (i == j):
				j += 1
			i += 1
		if (arr[k] == p):
			arr[k], arr[j] = arr[j], arr[k]
			j += 1

	arr[l], arr[i-1] = arr[i-1], arr[l]
	return (i, j)

if __name__ == "__main__":
	size = 100000
	arr = createRandomArr(size)
	startTime = time.time()
	tQuickSort(arr, 0, size)
	print ("Three Way Quick Sort Sort Time Taken :", (time.time() - startTime), "s for", size, "numbers")