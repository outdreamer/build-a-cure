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

			def level_order(node: TreeNode) -> None:
			    q: queue.Queue = queue.Queue()
			    q.put(node)
			    while not q.empty():
			        node_dequeued = q.get()
			        print(node_dequeued.data, end=",")
			        if node_dequeued.left:
			            q.put(node_dequeued.left)
			        if node_dequeued.right:
			            q.put(node_dequeued.right)

			def pre_order_iter(node: TreeNode) -> None:
			    stack: list[TreeNode] = []
			    n = node
			    while n or stack:
			        while n:  
			            print(n.data, end=",")
			            stack.append(n)
			            n = n.left
			        n = stack.pop()
			        n = n.right

			def in_order_iter(node: TreeNode) -> None:
			    stack: list[TreeNode] = []
			    n = node
			    while n or stack:
			        while n:
			            stack.append(n)
			            n = n.left
			        n = stack.pop()
			        print(n.data, end=",")
			        n = n.right

			def post_order_iter(node: TreeNode) -> None:
			    stack1, stack2 = [], []
			    n = node
			    stack1.append(n)
			    while stack1:  
			        n = stack1.pop()
			        if n.left:
			            stack1.append(n.left)
			        if n.right:
			            stack1.append(n.right)
			        stack2.append(n)
			    while stack2:  
			        print(stack2.pop().data, end=",")

	- implement a math calculator
	- implement a trie
	- What would be the optimal method to sort a list
	- Two Sum problem
	- Fizz Buzz, 2 sum and valid parenthesis
	- 2-D DP
	- Longest Common Subsequence
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
		- quick sort
			from __future__ import annotations
			from random import randrange
			def quick_sort(collection: list) -> list:
			    if len(collection) < 2:
			        return collection
			    pivot_index = randrange(len(collection))
			    pivot = collection.pop(pivot_index)
			    lesser = [item for item in collection if item <= pivot]
			    greater = [item for item in collection if item > pivot]
			    return [*quick_sort(lesser), pivot, *quick_sort(greater)]
		- merge sort
			def merge_sort(collection: list) -> list:
			    def merge(left: list, right: list) -> list:
			        result = []
			        while left and right:
			            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
			        result.extend(left)
			        result.extend(right)
			        return result
			    if len(collection) <= 1:
			        return collection
			    mid_index = len(collection) // 2
			    return merge(merge_sort(collection[:mid_index]), merge_sort(collection[mid_index:]))

		- tim sort
			def binary_search(lst, item, start, end):
			    if start == end:
			        return start if lst[start] > item else start + 1
			    if start > end:
			        return start
			    mid = (start + end) // 2
			    if lst[mid] < item:
			        return binary_search(lst, item, mid + 1, end)
			    elif lst[mid] > item:
			        return binary_search(lst, item, start, mid - 1)
			    else:
			        return mid

			def insertion_sort(lst):
			    length = len(lst)
			    for index in range(1, length):
			        value = lst[index]
			        pos = binary_search(lst, value, 0, index - 1)
			        lst = [*lst[:pos], value, *lst[pos:index], *lst[index + 1 :]]
			    return lst

			def merge(left, right):
			    if not left:
			        return right
			    if not right:
			        return left
			    if left[0] < right[0]:
			        return [left[0], *merge(left[1:], right)]
			    return [right[0], *merge(left, right[1:])]

			def tim_sort(lst):
			    length = len(lst)
			    runs, sorted_runs = [], []
			    new_run = [lst[0]]
			    sorted_array = []
			    i = 1
			    while i < length:
			        if lst[i] < lst[i - 1]:
			            runs.append(new_run)
			            new_run = [lst[i]]
			        else:
			            new_run.append(lst[i])
			        i += 1
			    runs.append(new_run)
			    for run in runs:
			        sorted_runs.append(insertion_sort(run))
			    for run in sorted_runs:
			        sorted_array = merge(sorted_array, run)
			    return sorted_array

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

		- bubble sort
			def bubble_sort_iterative(collection: list[Any]) -> list[Any]:
			    length = len(collection)
			    for i in reversed(range(length)):
			        swapped = False
			        for j in range(i):
			            if collection[j] > collection[j + 1]:
			                swapped = True
			                collection[j], collection[j + 1] = collection[j + 1], collection[j]
			        if not swapped:
			            break
			    return collection

			def bubble_sort_recursive(collection: list[Any]) -> list[Any]:
			    length = len(collection)
			    swapped = False
			    for i in range(length - 1):
			        if collection[i] > collection[i + 1]:
			            collection[i], collection[i + 1] = collection[i + 1], collection[i]
			            swapped = True
			    return collection if not swapped else bubble_sort_recursive(collection)

	- search algorithms

		- linear search

			- basic linear search

			    for index, item in enumerate(sequence):
			        if item == target:
			            return index
			    return -1

			- recursive linear search

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
				if list(sorted_collection) != sorted(sorted_collection):
			        raise ValueError("sorted_collection must be sorted in ascending order")

			this basic implementation:
			    left = 0
			    right = len(sorted_collection) - 1
			    while left <= right:
			        midpoint = left + (right - left) // 2
			        current_item = sorted_collection[midpoint]
			        if current_item == item:
			            return midpoint
			        elif item < current_item:
			            right = midpoint - 1
			        else:
			            left = midpoint + 1

			alternate simple implementation with recursion:
			    if len(a_list) == 0:
			        return False
			    midpoint = len(a_list) // 2
			    if a_list[midpoint] == item:
			        return True
			    if item < a_list[midpoint]:
			        return binary_search(a_list[:midpoint], item)
			    else:
			        return binary_search(a_list[midpoint + 1 :], item)

		    or the std lib implementation:
			    index = bisect.bisect_left(sorted_collection, item)
			    if index != len(sorted_collection) and sorted_collection[index] == item:
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
		- BFS
		- DFS
		- djikstra's algorithm

	- dynamic programming
		- solving problems by breaking them into sub-problems

	- greedy algorithms
		- making locally optimal choices like kruskal's algorithm


https://visualgo.net/en
https://github.com/keon/algorithms
https://github.com/TheAlgorithms/Python
https://www.geeksforgeeks.org/dsa/top-100-data-structure-and-algorithms-dsa-interview-questions-topic-wise/#
https://medium.com/@contactomyna/python-data-structures-and-algorithms-cheat-sheet-a0e23796dd96