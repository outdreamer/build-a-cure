Data structures and algorithms study guide

- problem-solving tips

	- if there is a nested iteration implied, look for a constraint that indicates a way around iteration
		- for example, checking for an output constraint that can be iterated/checked instead of the input values:
			- a sum constraint can indicate an output (as in the sum) to check rather than iterating through every possible value to sum
			- a constraint on relevant output values can indicate a smaller alternate output iteration to perform rather than iterating through every possible input value

- data structures

	- O(1) operations can become O(n) in worst case scenarios due to hash collisions which is rare bc of python's resizing and good hash functions
	- deep copy is required when the element like a list in another element like a list is mutable to avoid linking to a changing object
	- strings are immutable arrays of unicode characters, each character taking 1 - 4 bytes
		- find how many different substrings with no repeating characters are in a string
		- O(1) operations for strings include: 
			access by index, length
	- lists are ordered, mutable, and can contain duplicates, and has size and capacity, where it doubles the list capacity in a new list when the previous list is full
		- O(1) operations for list include:
			 clear, index, length, pop() from end, and store by index
	- tuples are ordered, immutable, and can contain duplicates, however if it contains mutable elements, those elements can be modified
		- O(1) operations for tuples include: 
			access by index
	- dictionaries now maintain the order of insertion as of python 3.7 and dict keys are immutable
		- O(1) operations for dict include: 
			clear, length, d.popitem(), d.values(), d.keys(), where delete/pop/get can be O(1) in the average case
	- sets are implemented as dictionaries and cant contain duplicates
		- O(1) operations for sets include: 
			clear, where add/contains/discard/pop can be O(1) in the average case
	- lists are slower for inserts, dicts/sets are fast for lookups/inserts but rely on hashing
	- tuple insertion requires creating a new object as tuples are immutable
	- linked lists have a next pointer to the next item in the list in one direction

	- trie
		- a trie is a specialized search tree data structure used to store and retrieve strings from a dictionary or set. Unlike a binary search tree, nodes in a trie do not store their associated key. Instead, each node's position within the trie determines its associated key, with the connections between nodes defined by individual characters rather than the entire key
		- tries are useful for autocomplete, approximate string matching, spell checking, and IP routing and are preferred to hash tables bc theyre organized by prefixes and dont have hash collisions
		- Every child node shares a common prefix with its parent node, and the root node represents the empty string

	- what is the difference between a stack and a queue
		- stacks use LIFO where the last element added is the first to be removed, push/pop operate on the top element, uses list.append for push, list.pop for pop, stacks are useful for undo operations and function calls, where collections.deque can be used for a stack using collections.deque.pop
		- queues use FIFO where the first element added is the first to be removed, enqueue adds an element to the end and dequeue removes the element from the front, use collections.deque.append for enqueue and collections.deque.popleft for dequeue, queues are useful for task scheduling and buffering, queue can be implemented with lists using list.pop(0) to remove the first item
		- collections.deque is optimized for fast appends/pops from both sides of the deque, so its more efficient than a list which has inefficient pop(0) operations for queues as all the elements have to be shifted by one when popping from the front of the list
		- double-ended queue (deque) in python this is implemented as a doubly linked list allowing O(1) operations at both ends
	
	- heap queue and priority queue algorithms
		- heaps are binary trees for which every parent node has a value less than or equal to any of its children, implemented as an array/list with heap properties
		- In a heap tree, the value in a node is always smaller than both of its children. This is different from a binary search tree, in which only the left node will be smaller than the value of its parent
		- The completeness property means that the depth of the tree is the base-2 logarithm of the number of elements, rounded up
		- adding a node to a heap: the node is added to the next open slot at the bottom. Otherwise, a new level is created and then the element is added to the new bottom layer.
			- Once the node is added, Python compares it to its parent. If the heap property is violated, then the node and its parent are switched, and the check begins again at the parent. 
			- This continues until the heap property holds or the root has been reached
			- when popping the smallest element, Python knows that, because of the heap property, the element is at the root of the tree. It replaces the element with the last element at the deepest layer and then checks if the heap property is violated down the branch
			- an element must always be smaller than the elements that are at twice its index plus one and twice its index plus two
			- you can transform a populated list into a heap via function heapify
		- a priority queue is a queue where items have priorities, where items with higher priority are dequeued first, and if items have the same priority, theyre dequeued in order of insertion like a queue, which acts like a sorted structure when dequeued
		- a priority queue is a common use for a heap
		- priority queues are used for task scheduling by priority, in dijkstra's shortest path algorithm to find the shortest path by selecting the nearest node, in huffman encoding to combine least frequent symbols using a priority queue to reduce data size, when merging multiple sorted lists by selecting the smallest element from each list, and a search algorithm (pathfinding) which prioritizes nodes based on cost to find the shortest path in navigation
		- max priority queues are where the highest priority item is dequeued first, and a min priority queue is where the lowest priority item is dequeued first
	
	- trees
		- binary trees: trees with at most two child nodes, a left and right node
	
	- graphs
		- the adjacency matrix of a graph stores the graph in the form of a 2D matrix where rows and columns denote vertices connected by an edge, where each entry in the matrix represents the weight of the edge between those vertices. 

	- o(n) complexity: one iteration of one list of size n
	- o(n^2) complexity: one nested iteration of two lists of size n
	- o(log n) complexity: binary search, recursively splitting a list at midpoint
	- o(n log n) complexity: best sorting case

- problems
	- implement a sliding window algorithm for looking at the last 5 days of stock prices
	- finding the number of unique digited numbers in a range
	- Create the largest number possible by switching digits that have the same parity. Process can be repeated until the largest number is created. Parity is whether it is even or odd
	- removing the smallest and largest elements and appending their sum to the end of a list, where its fastest to sort the list first using a mergesort
	- find the Least Number of Unique Integers after K Removals
	- find missing numbers of an array
		- find max, then find missing numbers in range up to max
	- Two Sum problem
	- dijkstra's algorithm
	- Greedy algorithm problem 
		- making locally optimal choices like kruskal's algorithm
	- 2-D DP
		- dynamic programming: simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner

	- reverse an array in place
		result = array[::-1]

	- Kadane's algorithm
		def maxSubarraySum(arr):
		    res = arr[0]
		    for i in range(len(arr)):
		        currSum = 0
		        for j in range(i, len(arr)):
		            currSum = currSum + arr[j]
		            res = max(res, currSum)
		    return res

	- Fizz Buzz
		def fizz_buzz(number: int, iterations: int) -> str:
		    # Prints Fizz if number is a multiple of ``3``, Prints Buzz if its a multiple of ``5``, Prints FizzBuzz if its a multiple of both ``3`` and ``5`` or ``15``, Else Prints The Number Itself.
		    if not isinstance(iterations, int):
		        raise ValueError("iterations must be defined as integers")
		    if not isinstance(number, int) or not number >= 1:
		        raise ValueError("""starting number must be and integer and be more than 0""")
		    if not iterations >= 1:
		        raise ValueError("Iterations must be done more than 0 times to play FizzBuzz")
		    out = ""
		    while number <= iterations:
		        if number % 3 == 0:
		            out += "Fizz"
		        if number % 5 == 0:
		            out += "Buzz"
		        if 0 not in (number % 3, number % 5):
		            out += str(number)
		        number += 1
		        out += " "
		    return out

- algorithms

	- sorting algorithms

		- time an algorithm
		    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""
		    times = repeat(setup=f"from __main__ import {algorithm}" if algorithm != "sorted" else "", stmt=f"{algorithm}({array})", repeat=3, number=10)

		- quick sort O(n log2(n))
			- uses divide and conquer to divide the input into two lists around the pivot element, the first list with small items and the second with large items, then sorts both lists recursively
			- quick sort partitions the list around the pivot, putting every smaller element into a low list and every larger element into a high list so the pivot is in its correct position, at which point this is repeated recursively to the low list and the high list
			- Selecting the pivot at random makes it more likely Quicksort will select a value closer to the median and finish faster
			- forcing the median value as the pivot for Quicksort guarantees you will have the best-case Big O scenario, which can be done in O(n) time (O(n) + O(n log2n) which can be simplified to O(n log2n))
			- the input list is partitioned in linear time, O(n), and this process repeats recursively an average of log2n times. This leads to a final complexity of O(n log2n)
			- Randomly selecting the pivot makes the worst case very unlikely. That makes random pivot selection good enough for most implementations of the algorithm
			- quick sort is much faster than merge sort 
			- easy to parallelize
			- doesnt guarantee that it will achieve the average runtime complexity
			- quick sort can degrade down to O(n^2)
			- trades off memory space for speed which is a limitation for large lists

		- merge sort O(n log2(n))
			- O(n log2n) is the best possible worst-case runtime that can be achieved by a sorting algorithm
			- uses divide-and-conquer to divide the input into two lists, then sorts both lists recursively, and finally merges these two sorted parts into a single sorted list
			- bubble sort and insertion sort are faster than merge sort for small lists bc of the recursion of merge sort and merge sort also uses more memory than bubble and insertion sort
			- easy to parallelize
			- trades off memory space for speed which is a limitation for large lists
			
		- insertion sort O(n^2)
			- insertion sort is faster than bubble sort
			- Timsort uses insertion sort internally to sort small portions of the input array

		- tim sort O(nlog2(n))
			- uses a combination of insertion sort and merge sort to merge already sorted sub-sections/runs into bigger sorted sub-sections and then the final sorted list
			- Timsort uses the newly introduced left and right parameters in insertion_sort() to sort the list in place without having to create new arrays like merge sort and Quicksort do
			- unlike merge sort, Timsort merges subarrays that were previously sorted, which decreases the total number of comparisons required to produce a sorted list
			- min_run is small to benefit from fast insertion_sort on small arrays
			- Picking a min_run value that’s a power of two ensures better performance when merging all the different runs that the algorithm creates bc merging balanced lists is more efficient than merging imbalanced lists
			- in practice, timsort picks a value between 32 and 64 inclusive, such that the length of the list divided by min_run is exactly a power of 2. If that’s not possible, it chooses a value that’s close to, but strictly less than, a power of 2
			- very fast for small arrays because the algorithm turns into a single insertion sort
			- bc it’s common to sort arrays that already have some preexisting order, Timsort is a great option

		- heap sort
			def heapify(unsorted: list[int], index: int, heap_size: int) -> None:
			    largest = index
			    left_index = 2 * index + 1
			    right_index = 2 * index + 2
			    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
			        largest = left_index
			    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
			        largest = right_index
			    if largest != index:
			        unsorted[largest], unsorted[index] = (unsorted[index], unsorted[largest])
			        heapify(unsorted, largest, heap_size)

			def heap_sort(unsorted: list[int]) -> list[int]:
			    n = len(unsorted)
			    for i in range(n // 2 - 1, -1, -1):
			        heapify(unsorted, i, n)
			    for i in range(n - 1, 0, -1):
			        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
			        heapify(unsorted, 0, i)
			    return unsorted

	- dynamic programming

		- solving problems by breaking them into sub-problems

		- optimal binary search tree O(n^2)

				import sys
				from random import randint

				class Node:
				    def __init__(self, key, freq):
				        self.key = key
				        self.freq = freq
				    def __str__(self):
				        return f"Node(key={self.key}, freq={self.freq})"

				def find_optimal_binary_search_tree(nodes):
				    nodes.sort(key=lambda node: node.key)
				    n = len(nodes)
				    keys = [nodes[i].key for i in range(n)]
				    freqs = [nodes[i].freq for i in range(n)]
				    # stores the overall tree cost (which is as minimized as possible), the cost for a key is the frequency of the key.
				    dp = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
				    # total[i][j] stores the sum of key frequencies between i and j inclusive in nodes array
				    total = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
				    # stores tree roots that will be used later for constructing binary search tree
				    root = [[i if i == j else 0 for j in range(n)] for i in range(n)]
				    for interval_length in range(2, n + 1):
				        for i in range(n - interval_length + 1):
				            j = i + interval_length - 1
				            dp[i][j] = sys.maxsize
				            total[i][j] = total[i][j-1] + freqs[j]
				            for r in range(root[i][j-1], root[i+1][j] + 1):
				                left = dp[i][r-1] if r != i else 0  # optimal cost for left subtree
				                right = dp[r+1][j] if r != j else 0  # optimal cost for right subtree
				                cost = left + total[i][j] + right
				                if dp[i][j] > cost:
				                    dp[i][j] = cost
				                    root[i][j] = r
				    for node in nodes:
				        print(node)
				    print(f"\nThe cost of optimal BST for given tree nodes is {dp[0][n-1]}.")

				nodes = [Node(i, randint(1, 50)) for i in range(10, 0, -1)]
				find_optimal_binary_search_tree(nodes)

https://visualgo.net/en
https://github.com/keon/algorithms
https://github.com/TheAlgorithms/Python
https://www.geeksforgeeks.org/dsa/top-100-data-structure-and-algorithms-dsa-interview-questions-topic-wise/#
https://medium.com/@contactomyna/python-data-structures-and-algorithms-cheat-sheet-a0e23796dd96
https://www.geeksforgeeks.org/searching-algorithms-in-python/
http://prepinsta.com/data-structures-and-algorithms-in-python/searching-algorithms-in-python/
https://www.geeksforgeeks.org/dsa/searching-algorithms/
https://realpython.com/sorting-algorithms-python/