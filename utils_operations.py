# -*- coding: utf-8 -*-


# %% including required libraries, modules and files with code
import numpy as np
import turtle
import math
import random
from time import time


# %% The class that contains functions to perform random matrix generation operations
class createamatrix():
	def __init__(self):
		pass

	def randommatrix(self, number_of_rows_matrix1, number_of_columns_matrix1, number_of_rows_matrix2,
					 number_of_columns_matrix2):
		self.matrix1 = np.random.randint(-10, 10, size=(
		number_of_rows_matrix1, number_of_columns_matrix1))  # Creating random matrix with the help of numpy library
		self.matrix2 = np.random.randint(-10, 10, size=(
		number_of_rows_matrix2, number_of_columns_matrix2))  # Creating random matrix with the help of numpy library
		return self.matrix1, self.matrix2


# %% The class that contains functions to perform matrix multiplication operations
class matrix_mult:
	def __init__(self):
		pass

	# This function to perform matrix multiplication operations.
	def multiplication(self, matrix1, matrix2):
		# Size of the result matrix.
		self.resultmatrix = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
		# Determine rows of first matrix.
		for i in range(len(matrix1)):
			# Determine columns of second matrix.
			for j in range(len(matrix2[0])):
				# Determine rows of second matrix.
				for k in range(len(matrix2)):
					self.resultmatrix[i][j] += matrix1[i][k] * matrix2[k][j]
		# Return the result matrix.
		return self.resultmatrix


# %% The class that contains functions to perform fibonacci number operations
class fibonacci:
	def __init__(self):
		pass

	def fibonacci_number(self, n):
		if n <= 0:
			print("Incorrect input")
		elif n == 1:
			return 0
		elif n == 2:
			return 1
		else:
			return self.fibonacci_number(n - 1) + self.fibonacci_number(n - 2)

	def fibonacci_array(self, n):
		if n == 1:
			self.fibonacci_numbers = [0]
		elif n == 2:
			self.fibonacci_numbers = [0, 1]
		else:
			self.fibonacci_numbers = [0, 1]
			for i in range(2, n):
				self.fibonacci_numbers.append(self.fibonacci_numbers[i - 1] + self.fibonacci_numbers[i - 2])
		return self.fibonacci_numbers


# %% The class that contains functions to perform binary search operations
class binarysearch:
	def __init__(self):
		pass

	def createarray(self, l, u, n):  # take lower bound from user #take array size from user
		self.unsorted_array = set()  # Generating random arrays containing different numbers with format set
		while True:
			self.unsorted_array.add(random.randint(l, u))
			if len(self.unsorted_array) == n:
				break
		return list(self.unsorted_array)  # returning the set in list form

	def insertionSort(self, array):  # create an funciton to do insertion sort
		for i in range(1, len(array)):  # making a for loop because of to swap an item with previous one,starting from 1
			key = array[i]  # key will be used for comparison with previous items and sent to the place it belongs
			j = i - 1
			while j >= 0 and key < array[
				j]:  # while loop for comparing the current element with the sorted portion and swapping
				array[j + 1] = array[j]  # moving the bigger item 1 step right to make place for key
				j -= 1
			array[
				j + 1] = key  # take array[j] all the way left to the place where it has a smaller/no value to its left
		return array

	def binary_search(self, array, value):
		first_index = 0
		last_index = len(array) - 1
		while first_index <= last_index:
			mid = first_index + (last_index - first_index) // 2
			mid_val = array[mid]
			if mid_val == value:
				return mid + 1
			elif value < mid_val:
				last_index = mid - 1
			else:
				first_index = mid + 1


# %%The class that contains functions to perform randomized selection operations
class randomized_selection():
	def __init__(self):
		pass

	def partition(self, array, p, r):
		x = array[r]
		i = p - 1
		for j in range(p, r):
			if array[j] <= x:
				i += 1
				array[i], array[j] = array[j], array[i]
		array[i + 1], array[r] = array[r], array[i + 1]
		return (i + 1)

	def randomized_partition(self, array, p, r):
		i = random.randint(p, r)
		array[r], array[i] = array[i], array[r]
		return self.partition(array, p, r)

	def randomized_select(self, array, p, q, i):
		if p == q:
			return array[p]
		r = self.randomized_partition(array, p, q)
		k = r - p + 1
		if i == k:
			return array[r]
		elif i < k:
			return self.randomized_select(array, p, r - 1, i)
		else:
			return self.randomized_select(array, r + 1, q, i - k)

	def createarray(self, l, u, n):  # take lower bound from user #take array size from user
		self.unsorted_array = set()  # Generating random arrays containing different numbers with format set
		while True:
			self.unsorted_array.add(random.randint(l, u))
			if len(self.unsorted_array) == n:
				break
		return list(self.unsorted_array)  # returning the set in list form

	def insertionSort(self, array):  # create an funciton to do insertion sort
		for i in range(1, len(array)):  # making a for loop because of to swap an item with previous one,starting from 1
			key = array[i]  # key will be used for comparison with previous items and sent to the place it belongs
			j = i - 1
			while j >= 0 and key < array[
				j]:  # while loop for comparing the current element with the sorted portion and swapping
				array[j + 1] = array[j]  # moving the bigger item 1 step right to make place for key
				j -= 1
			array[
				j + 1] = key  # take array[j] all the way left to the place where it has a smaller/no value to its left
		return array


# %% The class that contains functions to perform time comparison operations
class sortingalgorithmsfortimecomparison():
	def __init__(self):
		pass

	def insertionSort(self, array):  # create an funciton to do insertion sort
		for i in range(1, len(array)):  # making a for loop because of to swap an item with previous one,starting from 1
			key = array[i]  # key will be used for comparison with previous items and sent to the place it belongs
			j = i - 1
			while j >= 0 and key < array[
				j]:  # while loop for comparing the current element with the sorted portion and swapping
				array[j + 1] = array[j]  # moving the bigger item 1 step right to make place for key
				j -= 1
			array[
				j + 1] = key  # take array[j] all the way left to the place where it has a smaller/no value to its left
		return array

	def BubbleSort(self, array):  # create an funciton to do bubble sort
		for i in range(0, len(array) - 1):  # loop for all array elements
			for j in range(len(array), i + 1, -1):  # second cycle for swap operations
				if array[j - 1] < array[j - 2]:  # if the left greater than right
					array[j - 2], array[j - 1] = array[j - 1], array[j - 2]  # swap to the index of value
		return array

	def mergeSort(self, array, p, r):  # create an function to do merge sort
		if p < r:  # p is the first index, r is the last index.
			q = (p + r) // 2  # q is the middle index
			self.mergeSort(array, p, q)  # recursive function for new right array created
			self.mergeSort(array, q + 1, r)  # recursive function for new right array created
			self.merge(array, p, q, r)  # merge funciton for sorted array to merge
		return array

	def merge(self, array, p, q, r):
		n1 = q - p + 1  # left array of length is n1
		n2 = r - q  # right array of lenght is n2
		left_array = np.empty(n1 + 1)  # computes the length n1+1 of the subarray
		right_array = np.empty(n2 + 1)  # computes the length n2+1 of the subarray
		for i in range(n1):  # The for loop of copies the subarray divided array into left array
			left_array[i] = array[p + i]
		for j in range(n2):  # The for loop of copies the subarray divided array into right array
			right_array[j] = array[q + 1 + j]
		left_array[n1] = np.inf  # use inf value as the sentinel value
		right_array[n2] = np.inf  # use inf value as the sentinel value
		i = 0  # empty subarray contains the 0 smallest elements of left array and right array
		j = 0
		for k in range(p, r + 1):  # the subarrays indexes compare
			if left_array[i] <= right_array[
				j]:  # campare left array ith index and right array jth index for sorted array
				array[k] = left_array[i]  # the smaller one is added to the arrays about to be sorted
				i += 1
			else:
				array[k] = right_array[j]  # the smaller one is added to the arrays about to be sorted
				j += 1
		return array

	def SelectionSort(self, array):
		for i in range(len(array)):
			min = i
			for j in range(i + 1, len(array)):
				if array[min] > array[j]:
					min = j

			array[i], array[min] = array[min], array[i]

	def QuickSort(self, array, p, r):
		if p < r:
			q = self.partition(array, p, r)
			self.QuickSort(array, p, q - 1)
			self.QuickSort(array, q + 1, r)

	def partition(self, array, p, r):
		pivotelement = array[r]
		i = p - 1
		for j in range(p, r):
			if array[j] <= pivotelement:
				i += 1
				array[i], array[j] = array[j], array[i]
		array[i + 1], array[r] = array[r], array[i + 1]
		return i + 1

	def Heapify(self, array, n, i):
		largest = i
		left = 2 * i + 1
		right = 2 * i + 2

		if left < n and array[i] < array[left]:
			largest = left
		if right < n and array[largest] < array[right]:
			largest = right
		if largest != i:
			array[i], array[largest] = array[largest], array[i]
			self.Heapify(array, n, largest)

	def HeapSort(self, array):
		n = len(array)
		for i in range(n // 2 - 1, -1, -1):
			self.Heapify(array, n, i)
		for i in range(n - 1, 0, -1):
			array[i], array[0] = array[0], array[i]
			self.Heapify(array, i, 0)

	def CountingSort(self, array):
		max_value = int(max(array))
		min_value = int(min(array))
		range_of_elements = max_value - min_value + 1

		counting_temp_array = [0 for _ in range(range_of_elements)]
		sorted_array = [0 for _ in range(len(array))]

		for i in range(0, len(array)):
			counting_temp_array[array[i] - min_value] += 1

		for i in range(1, len(counting_temp_array)):
			counting_temp_array[i] += counting_temp_array[i - 1]

		for i in range(len(array) - 1, -1, -1):
			sorted_array[counting_temp_array[array[i] - min_value] - 1] = array[i]
			counting_temp_array[array[i] - min_value] -= 1

		for i in range(0, len(array)):
			array[i] = sorted_array[i]

	def BucketSort(self, array):
		max_value = max(array)
		size = max_value / len(array)

		buckets_list = []
		for x in range(len(array)):
			buckets_list.append([])

		for i in range(len(array)):
			j = int(array[i] / size)
			if j != len(array):
				buckets_list[j].append(array[i])

			else:
				buckets_list[len(array) - 1].append(array[i])

		for z in range(len(array)):
			self.insertionSort(buckets_list[z])

		final_output = []
		for x in range(len(array)):
			final_output = final_output + buckets_list[x]

		for i in range(0, len(array)):
			array[i] = final_output[i]

	def ShellSort(self, array):
		n = len(array)
		gap = n // 2

		while gap > 0:
			for i in range(gap, n):
				temp = array[i]
				j = i
				while j >= gap and array[j - gap] > temp:
					array[j] = array[j - gap]
					j -= gap
				array[j] = temp
			gap //= 2

	def countingSort(self, array, digit):
		count = []
		result_array = []
		j = len(array) - 1
		for i in range(10):
			count.append(0)
		for i in range(len(array)):
			result_array.append(0)
		for i in range(len(array)):
			count[(array[i] // digit) % 10] += 1
		for i in range(len(count)):
			if i > 0:
				count[i] += count[i - 1]
		for i in range(len(array)):
			count[(array[j] // digit) % 10] -= 1
			result_array[count[(array[j] // digit) % 10]] = array[j]
			j -= 1
		for i in range(len(array)):
			array[i] = result_array[i]

	def RadixSort(self, array):
		max_number = max(array)
		digit = 1
		while max_number // digit > 0:
			self.countingSort(array, digit)
			digit *= 10


# %%
class timer():
	def __init__(self):  # set the initializer method
		self.n = [100, 300, 500, 2000]  # define random array lengths

	def create_array(self, length, maximum):  # define a random array creator function
		random.seed(0)
		random.sample
		self.new_array = [random.randint(0, maximum) for i in
						  range(length)]  # create a random array between -500 and maximum
		return self.new_array  # return that to use this array on below

	def comparison(self, situations):
		self.times = {"Bubble": [], "Insertion": [], "Merge": [], "Selection": [], "Counting": [], "Heap": [],
					  "Bucket": [], "Radix": [], "Quick": [],
					  "Shell": []}  # create a dictionary that holds sorting algorithm names
		for size in self.n:  # for loop for send the array's lengths as a parameters
			if situations[0]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().BubbleSort(array)  # make bubble sorting
				t1 = time()  # take the time after the sorting
				self.times["Bubble"].append(t1 - t0)  # add this time to a dictionary where Bubble's location

			if situations[1]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().insertionSort(array)  # make insertion sorting
				t1 = time()  # take the time after the sorting
				self.times["Insertion"].append(t1 - t0)  # add this time to a dictionary where Insertion's location

			if situations[2]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().mergeSort(array, 0, len(array) - 1)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Merge"].append(t1 - t0)  # add this time to a dictionary where Merge's location

			if situations[3]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().SelectionSort(array)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Selection"].append(t1 - t0)  # add this time to a dictionary where Selection's location

			if situations[4]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().CountingSort(array)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Counting"].append(t1 - t0)  # add this time to a dictionary where Counting's location

			if situations[5]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().HeapSort(array)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Heap"].append(t1 - t0)  # add this time to a dictionary where Heap's location

			if situations[6]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().BucketSort(array)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Bucket"].append(t1 - t0)  # add this time to a dictionary where Bucket's location

			if situations[7]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().RadixSort(array)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Radix"].append(t1 - t0)  # add this time to a dictionary where Radix's location

			if situations[8]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().QuickSort(array, 0, len(array) - 1)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Quick"].append(t1 - t0)  # add this time to a dictionary where Quick's location
			if situations[9]:
				array = self.create_array(size, size)  # create array
				t0 = time()  # take the time before the sorting
				sortingalgorithmsfortimecomparison().ShellSort(array)  # make merge sorting
				t1 = time()  # take the time after the sorting
				self.times["Shell"].append(t1 - t0)  # add this time to a dictionary where Quick's location
		return self.times
