#!/usr/bin/python3.6

from create import createRandomArr

#!/usr/bin/python3.6

from create import createRandomArr
import time

def insertionSort(arr):
	N = len(arr)
	for i in range(1, N):
		j = i-1
		key = arr[i]
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return (arr)

if __name__ == "__main__":
	size = 10000
	arr = createRandomArr(size)
	startTime = time.time()
	insertionSort(arr)
	print ("Insertion Sort Time Taken :", (time.time() - startTime), "s for", size, "numbers")