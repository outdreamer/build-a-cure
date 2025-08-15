Data structures and algorithms study guide

- problem-solving tips

	- if there is a nested iteration implied, look for a constraint that indicates a way around iteration
		- for example, checking for an output constraint that can be iterated/checked instead of the input values:
			- a sum constraint can indicate an output (as in the sum) to check rather than iterating through every possible value to sum
			- a constraint on relevant output values can indicate a smaller alternate output iteration to perform rather than iterating through every possible input value

- data structures
	- // is integer division which rounds down to the nearest integer, where negative results of integer division are rounded down toward negative infinity and where / is float division
	- O(1) operations are average case and can become O(n) in worst case scenarios due to hash collisions which is rare bc of python's resizing and good hash functions
	- deep copy is required when the element like a list in another element like a list is mutable to avoid linking to a changing object
	- strings are immutable arrays of unicode characters, each character taking 1 - 4 bytes
		- find how many different substrings with no repeating characters are in a string
	- lists are ordered, mutable, and can contain duplicates, and has size and capacity, where it doubles the list capacity in a new list when the previous list is full
	- tuples are ordered, immutable, and can contain duplicates, however if it contains mutable elements, those elements can be modified
	- dictionaries now maintain the order of insertion and dict keys are immutable
	- sets are implemented as dictionaries and cant contain duplicates
	- linked lists
	- stacks (LIFO)
	- queues (FIFO)
	- double ended queue (deque) in python this is implemented as a doubly linked list allowing O(1) operations at both ends
	- heaps (priority queues) in python heaps are implemented as an array/list with heap properties
	- trees
		- binary trees
	- graphs
	- priority queue

- problems
	- invert a binary tree
	- implement a binary tree

			from __future__ import annotations
			import queue

			class TreeNode:
			    def __init__(self, data):
			        self.data = data
			        self.right = None
			        self.left = None

			def build_tree() -> TreeNode:
			    check = input("Enter the value of the root node: ").strip().lower()
			    q: queue.Queue = queue.Queue()
			    tree_node = TreeNode(int(check))
			    q.put(tree_node)
			    while not q.empty():
			        node_found = q.get()
			        check = input(f"Enter the left node of {node_found.data}: ").strip().lower() or "n"
			        if check == "n":
			            return tree_node
			        left_node = TreeNode(int(check))
			        node_found.left = left_node
			        q.put(left_node)
			        check = input(f"Enter the right node of {node_found.data}: ").strip().lower() or "n"
			        if check == "n":
			            return tree_node
			        right_node = TreeNode(int(check))
			        node_found.right = right_node
			        q.put(right_node)
			    raise ValueError("Something went wrong")

			def pre_order(node: TreeNode) -> None:
			    if not isinstance(node, TreeNode) or not node:
			        return
			    print(node.data, end=",")
			    pre_order(node.left)
			    pre_order(node.right)

			def in_order(node: TreeNode) -> None:
			    in_order(node.left)
			    print(node.data, end=",")
			    in_order(node.right)

			def post_order(node: TreeNode) -> None:
			    post_order(node.left)
			    post_order(node.right)
			    print(node.data, end=",")

	- implement a math calculator
	- implement a trie
	- What would be the optimal method to sort a list

			Linear Search is the simplest algorithm, involving a sequential check of each element in the list until the target value is found or the end of the list is reached.
			 It is suitable for unsorted data and is often implemented by iterating through the list with a loop, returning the index of the first occurrence of the target or -1 if not found.
			 While straightforward, it is inefficient for large datasets, with a time complexity of O(n).

			Binary Search is a more efficient algorithm designed for sorted lists.
			 It works by repeatedly dividing the search interval in half. The algorithm compares the target value to the middle element of the list; if they are equal, the search is complete. If the target is less than the middle element, the search continues in the left half; if greater, it continues in the right half.
			 This process repeats until the target is found or the search interval is empty. Binary Search has a time complexity of O(log n), making it significantly faster than Linear Search for large sorted datasets.

			Interpolation Search is an enhanced version of Binary Search, particularly effective for large, uniformly distributed sorted arrays.
			 Instead of always checking the middle element, it estimates the position of the target value based on the value of the key and the range of the search space using a formula.
			 This can lead to faster search times in ideal conditions, with an average time complexity of O(log log n) for uniformly distributed data, although it degrades to O(n) in the worst case.

			Jump Search is another algorithm suitable for sorted arrays.
			 It works by jumping ahead by a fixed number of steps (typically the square root of the list length) and then performing a linear search within the smaller range once the target is potentially within the current block.
			 This approach balances the efficiency of Binary Search with the simplicity of Linear Search, resulting in a time complexity of O(√n).

			The choice of algorithm depends on factors such as whether the data is sorted, the size of the dataset, and the frequency of searches.
			 For unsorted data, Linear Search is the primary option. For sorted data, Binary Search is generally the most efficient choice, while Interpolation Search can be faster for uniformly distributed data, and Jump Search offers a good compromise between simplicity and performance.

	- Two Sum problem
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

	- valid parenthesis
	- 2-D DP
	- Longest Common Subsequence

		if x is not None and y is not None
		    m = len(x)
		    n = len(y)
		    dp = [[0] * (n + 1) for _ in range(m + 1)]
		    for i in range(1, m + 1):
		        for j in range(1, n + 1):
		            match = 1 if x[i-1] == y[j-1] else 0
		            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + match)
		    seq = ""
		    i, j = m, n
		    while i > 0 and j > 0:
		        match = 1 if x[i-1] == y[j-1] else 0
		        if dp[i][j] == dp[i-1][j-1] + match:
		            if match == 1:
		                seq = x[i-1] + seq
		            i -= 1
		            j -= 1
		        elif dp[i][j] == dp[i-1][j]:
		            i -= 1
		        else:
		            j -= 1
		    return dp[m][n], seq


	- Implement a sliding window algorithm for looking at the last 5 days of stock prices
	- finding the number of unique digited numbers in a range
	- Create the largest number possible by switching digits that have the same parity. Process can be repeated until the largest number is created.
	- Greedy problem 
	- reverse an array in place
	- removing the smallest and largest elements and appending their sum to the end of a list, where its fastest to sort the list first using a mergesort
	- find the Least Number of Unique Integers after K Removals
	- find missing numbers of an array
	- create a character array
	- Kadane
	- visualise a double-linked list

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
			
			from __future__ import annotations
			from random import randint
			def quick_sort(array: list) -> list:
			    if len(array) <= 1:
			        return array
			    low, same, high = [], [], []
			    pivot = array[randint(0, len(array) - 1)]
			    for item in array:
			        if item < pivot:
			            low.append(item)
			        elif item == pivot:
			            same.append(item)
			        elif item > pivot:
			            high.append(item)
			    return quick_sort(low) + same + quick_sort(high)

		- merge sort O(n log2(n))
			- O(n log2n) is the best possible worst-case runtime that can be achieved by a sorting algorithm
			- uses divide-and-conquer to divide the input into two lists, then sorts both lists recursively, and finally merges these two sorted parts into a single sorted list
			- bubble sort and insertion sort are faster than merge sort for small lists bc of the recursion of merge sort and merge sort also uses more memory than bubble and insertion sort
			- easy to parallelize
			- trades off memory space for speed which is a limitation for large lists
			
			def merge_sort(array):
				def merge(left, right):
				    if len(left) == 0:
				        return right
				    if len(right) == 0:
				        return left
				    result = []
				    index_left = index_right = 0
				    while len(result) < len(left) + len(right):
				        if left[index_left] <= right[index_right]:
				            result.append(left[index_left])
				            index_left += 1
				        else:
				            result.append(right[index_right])
				            index_right += 1
				        if index_right == len(right):
				            result += left[index_left:]
				            break
				        if index_left == len(left):
				            result += right[index_right:]
				            break
				    return result
			    if len(array) <= 1:
			        return array
			    midpoint = len(array) // 2
			    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))

		- insertion sort O(n^2)
			- insertion sort is faster than bubble sort
			- Timsort uses insertion sort internally to sort small portions of the input array
			
			def insertion_sort(array):
			    for i in range(1, len(array)):
			        key_item = array[i]
			        j = i - 1
			        while j >= 0 and array[j] > key_item:
			            array[j + 1] = array[j]
			            j -= 1
			        array[j + 1] = key_item
			    return array

		- tim sort O(nlog2(n))
			- uses a combination of insertion sort and merge sort to merge already sorted sub-sections into bigger sorted sub-sections and then the final sorted list
			- Timsort uses the newly introduced left and right parameters in insertion_sort() to sort the list in place without having to create new arrays like merge sort and Quicksort do
			- unlike merge sort, Timsort merges subarrays that were previously sorted, which decreases the total number of comparisons required to produce a sorted list
			- min_run is small to benefit from fast insertion_sort on small arrays
			- Picking a min_run value that’s a power of two ensures better performance when merging all the different runs that the algorithm creates bc merging balanced lists is more efficient than merging imbalanced lists
			- in practice, timsort picks a value between 32 and 64 inclusive, such that the length of the list divided by min_run is exactly a power of 2. If that’s not possible, it chooses a value that’s close to, but strictly less than, a power of 2
			- very fast for small arrays because the algorithm turns into a single insertion sort
			- bc it’s common to sort arrays that already have some preexisting order, Timsort is a great option
			
			def tim_sort(array):
			    min_run = 32
			    n = len(array)
			    for i in range(0, n, min_run):
			        insertion_sort(array, i, min((i + min_run - 1), n - 1))
			    size = min_run
			    while size < n:
			        for start in range(0, n, size * 2):
			            midpoint = start + size - 1
			            end = min((start + size * 2 - 1), (n-1))
			            merged_array = merge(left=array[start:midpoint + 1], right=array[midpoint + 1:end + 1])
			            array[start:start + len(merged_array)] = merged_array
			        size *= 2
			    return array

			def insertion_sort(array, left=0, right=None):
			    if right is None:
			        right = len(array) - 1
			    for i in range(left + 1, right + 1):
			        key_item = array[i]
			        j = i - 1
			        while j >= left and array[j] > key_item:
			            array[j + 1] = array[j]
			            j -= 1
			        array[j + 1] = key_item
			    return array

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

		- bubble sort O(n^2)
			def bubble_sort_iterative(array: list[Any]) -> list[Any]:
			    length = len(array)
			    for i in range(length):
			        swapped = False
			        for j in range(n - i - 1):
			            if array[j] > array[j + 1]:
			                swapped = True
			                array[j], array[j + 1] = array[j + 1], array[j]
			        if not swapped:
			            break
			    return array

	- search algorithms

		- linear search

			- basic linear search

			    for index, item in enumerate(sequence):
			        if item == target:
			            return index
			    return -1

			- recursive linear search
				rec_linear_search
					if not (0 <= high < len(sequence) and 0 <= low < len(sequence)):
				        raise Exception("Invalid upper or lower bound!")
				    if high < low:
				        return -1
				    if sequence[low] == target:
				        return low
				    if sequence[high] == target:
				        return high
				    return rec_linear_search(sequence, low + 1, high - 1, target)

		- binary search

			check if list is sorted:
				if list(array) != sorted(array):
			        raise ValueError("array must be sorted in ascending order")

			this basic implementation:
			    left = 0
			    right = len(array) - 1
			    while left <= right:
			        midpoint = left + (right - left) // 2
			        current_item = array[midpoint]
			        if current_item == item:
			            return midpoint
			        elif item < current_item:
			            right = midpoint - 1
			        else:
			            left = midpoint + 1

		    or the std lib implementation:
			    index = bisect.bisect_left(array, item)
			    if index != len(array) and array[index] == item:
			        return index

			then return -1 if item not found:
			    return -1

		- exponential search

		    if list(sorted_collection) != sorted(sorted_collection):
		        raise ValueError("sorted_collection must be sorted in ascending order")
		    if sorted_collection[0] == item:
		        return 0
		    bound = 1
		    while bound < len(sorted_collection) and sorted_collection[bound] < item:
		        bound *= 2
		    left = bound // 2
		    right = min(bound, len(sorted_collection) - 1)
		    return binary_search_by_recursion(sorted_collection, item, left, right)

	- graph algorithms

		- BFS (breadth first search)
			from queue import Queue
			vertices: dict[int, list[int]] = {}
		    def bfs(self, start_vertex: int) -> set[int]:
		        visited = set(start_vertex)
		        queue: Queue = Queue()
		        queue.put(start_vertex)
		        while not queue.empty():
		            vertex = queue.get()
		            for adjacent_vertex in vertices[vertex]:
		                if adjacent_vertex not in visited:
		                    queue.put(adjacent_vertex)
		                    visited.add(adjacent_vertex)
		        return visited

		- DFS (depth first search)
			vertices: dict[str, list[str]] = {}
			def depth_first_search(vertices: dict, start_vertex: str) -> set[str]:
			    visited = set(start_vertex)
			    stack = []
			    stack.append(start_vertex)
			    while stack:
			        # Differences from BFS:
			        # 1) pop last element instead of first one
			        # 2) add adjacent elements to stack without visiting them
			        vertex = stack.pop()
			        visited.add(vertex)
			        for adjacent_vertex in reversed(vertices[vertex]):
			            if adjacent_vertex not in visited:
			                stack.append(adjacent_vertex)
			    return visited

		- djikstra's algorithm

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


	- greedy algorithms
		- making locally optimal choices like kruskal's algorithm


https://visualgo.net/en
https://github.com/keon/algorithms
https://github.com/TheAlgorithms/Python
https://www.geeksforgeeks.org/dsa/top-100-data-structure-and-algorithms-dsa-interview-questions-topic-wise/#
https://medium.com/@contactomyna/python-data-structures-and-algorithms-cheat-sheet-a0e23796dd96
https://www.geeksforgeeks.org/searching-algorithms-in-python/
http://prepinsta.com/data-structures-and-algorithms-in-python/searching-algorithms-in-python/
https://www.geeksforgeeks.org/dsa/searching-algorithms/
https://realpython.com/sorting-algorithms-python/