#!/usr/bin/python3.6

import random

def createSortedArr(n):
	arr = []
	for i in range(n):
		arr.append(i)
	return (arr)

def createRandomArr(n):
	arr = createSortedArr(n)
	random.shuffle(arr)
	return (arr)