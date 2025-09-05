def is_valid_parentheses(string= "{[()]}"):
	stack = []
	forward_chars = ['(', '{', '[']
	mapping = {')':'(', '}':'{', ']':'['}
	for s in string:
		if s in forward_chars:
			stack.append(s)
		else:
			if stack.pop() == mapping[s]:
				pass
			else:
				return False
	return len(stack) == 0

# the first half should equal the second half backwards
# so iteratively popping the first half off a stack should equal the second half

# swap two numbers
a = a + b
b = a - b
a = a - b 

# linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Method to add a node at the beginning of the LL
	def insertAtBegin(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def reverse(self): # 1 2 3 4 
		prev = None
		current = self.head # start current at the first (head) node 1
		while (current is not None):
			next_node = current.next # save the value of current's next node, 2, 3
			current.next = prev # swap current's next value and the previous value current.next = None, current.next = 1
			prev = current # set previous to current prev = 1, prev = 2
			current = next_node # set current to the saved next_node value current = 2, current = 3
		self.head = prev

# trie
def create():
	return dict()

def insert(trie, word):
	for w in word:
		if w not in trie:
			trie[w] = {}
		trie = trie[w]
	trie["_end"] = True

def search_trie(trie, word):
	for w in word:
		if w not in trie:
			return False
		trie = trie[w]
	return True

def _walk_trie(node, partial_word, word_list):
	if node is not True:
		for char in node:
			if '_end' in node:
				word_list.append(partial_word)
			else:
				new_partial_word = partial_word + char
				_walk_trie(node[char], new_partial_word, word_list)

def auto_complete(trie, partial_word):
	word_list = []
	for w in partial_word:
		if w in trie:
			trie = trie[w]
		else:
			return word_list
	_walk_trie(trie, partial_word, word_list)
	return word_list

trie = create()
insert(trie, 'hello')
insert(trie, 'how')
insert(trie, 'why')
insert(trie, 'who')
print('trie', trie)
completed = auto_complete(trie, 'wh')
print('completed', completed)
searched = search_trie(trie, 'hell')
print('searched', searched)


# priority queue, remove max priority item on delete 
def insert(queue, d):
	queue.append(d)

def delete(queue):
	try:
		m = 0
		for i in range(len(queue)):
			if queue[i] > queue[m]:
				m = i
		item = queue[m]
		del queue[m]
		return item
	except IndexError:
		print("Queue empty.")
		exit()

queue = []
insert(queue, 14)
insert(queue, 7)
print(queue)
print("Removed elements:")
while not len(queue) == 0:
	print(delete(queue))


# stack
from collections import deque

stack = deque()
stack.append(1)  # Push
stack.append(2)
print(stack.pop())  # Output: 2 (LIFO)


# queue

from collections import deque

dq = deque()
dq.append(1)  # Enqueue
dq.append(2)
print(dq.popleft())  # Output: 1 (FIFO)

from queue import Queue

q = Queue()
q.put(1)
q.put(2)
print(q.get()) 


# heap (pops smallest element first)

import heapq

# Min-Heap
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

print(heapq.heappop(heap))  # Output: 5 (smallest element)

# a max heap can be implemented with heapq and negative values
heapq.heappush(heap, -10)  # Push negative values
max_value = -heapq.heappop(heap)  # Invert back

# doubly linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def delete_node(self, key):
		temp = self.head
		while temp:
			if temp.data == key:
				if temp.prev is None:
					self.head = temp.next
					if self.head:
						self.head.prev = None
				elif temp.next is None:
					temp.prev.next = None
				else:
					temp.prev.next = temp.next
					temp.next.prev = temp.prev
				return
			temp = temp.next

	def traverse(self):
		temp = self.head
		while temp:
			print(temp.data, end=" <-> ")
			temp = temp.next
		print("None")


# implement a binary tree
class TreeNode:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

class BinaryTree:

	def build_tree(left_int: int, right_int: int, root_int: int) -> TreeNode:
		q: queue.Queue = queue.Queue()
		tree_node = TreeNode(int(root_int))
		left_node = TreeNode(int(left_int))
		tree_node.left = TreeNode(int(left_int))
		q.put(left_node)
		right_node = TreeNode(int(right_int))
		tree_node.right = right_node
		q.put(right_node)
		q.put(tree_node)
		raise ValueError("Something went wrong")

	def pre_order_dfs(node: TreeNode) -> None: # DFS current-left-right
		if not isinstance(node, TreeNode) or not node:
			return
		print(node.data, end=",")
		pre_order_dfs(node.left)
		pre_order_dfs(node.right)

	def in_order_dfs(node: TreeNode) -> None: # DFS left-current-right
		if not isinstance(node, TreeNode) or not node:
			return
		in_order_dfs(node.left)
		print(node.data, end=",")
		in_order_dfs(node.right)

	def post_order_dfs(node: TreeNode) -> None: # DFS left-right-current
		if not isinstance(node, TreeNode) or not node:
			return
		post_order_dfs(node.left)
		post_order_dfs(node.right)
		print(node.data, end=",")

	def traverse_bfs(root_node: TreeNode) -> None: # BFS level order traversal
		if root_node is None:
			return
		queue = [root_node]
		while queue: # start by popping the root, then add both of its children to the queue to pop next, until the queue is empty
			node = queue.pop(0)
			print(node.data, end=",")
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

	def insert(root, val): # finds the first node with an empty right or left node and inserts it there, starting at the left child node
		queue = deque([root])
		while queue:
			temp = queue.popleft()
			if temp.left is None:
				temp.left = Node(val)
				break
			else:
				queue.append(temp.left)
			if temp.right is None:
				temp.right = Node(val)
				break
			else:
				queue.append(temp.right)
		return root

	def search_dfs(root, value):
		if root is None:
			return False
		if root.data == value:
			return True
		left_res = search_dfs(root.left, value)
		right_res = search_dfs(root.right, value)
		return left_res or right_res

	# delete in a binary tree by replacing the node’s value with the value of the last node in the tree (found by traversing to the rightmost leaf)

	# invert a binary tree
	def invert_tree(root):
		if root:
			temp = root.left
			root.left = invert_tree(root.right)
			root.right = invert_tree(temp)
			return root

#from __future__ import annotations
#from random import randint
#from queue import Queue
#import bisect

#check in every sort function
#	if len(array) <= 1:
#		return array

# for binary and exponential sort
# if list(array) != sorted(array):
#	raise ValueError("array needs to be sorted in ascending order")

# in merge functions:
#    if not left:
#        return right
#    if not right:
#        return left


# sort recommendations

"""
	"General Purpose (Large Data)": ["Merge Sort", "Quick Sort", "Heap Sort"],
	"Small Arrays (< 50 elements)": ["Insertion Sort", "Selection Sort"],
	"Nearly Sorted Data": ["Insertion Sort", "Shell Sort"],
	"Integers with Limited Range": ["Counting Sort", "Radix Sort"],
	"Uniformly Distributed Data": ["Bucket Sort"],
	"Memory Constrained": ["Heap Sort", "Quick Sort", "Shell Sort"],
	"Stability Required": ["Merge Sort", "Counting Sort", "Radix Sort"],
"""

def quick_sort(array: list) -> list:
	# selects a random or median pivot
	# then divides the list into a low list and a same list and a high list around the pivot
	# then applies quick_sort to the low and high list recursively, returning quick_sort(low) + same + quick_sort(high)
	# much faster than merge sort, O(n log2(n)) but can degrade to O(n^2)
	low, same, high = [], [], []
	pivot = array[randint(0, len(array) - 1)] # can also be median
	for item in array:
		if item < pivot:
			low.append(item)
		elif item == pivot:
			same.append(item)
		elif item > pivot:
			high.append(item)
	return quick_sort(low) + same + quick_sort(high)

def merge_sort(array):
	# identifies the midpoint of the list
	# then divides input into two lists at the midpoint
	# then sorts both lists recursively with merge_sort
	# then applies these merge_sorted lists as parameters of merge()
	# bubble/insertion are faster for small lists, merge_sort uses a lot of memory, O(n log2n)
	mid = len(array) // 2
	return merge(left=merge_sort(array[:mid]), right=merge_sort(array[mid:]))

def merge(left, right):
	# initialize index_left and index_right at 0
	# while result length is less than sum of left and right length
	# append the lower of left[index_left] and right[index_right] to the result list:
	# 	if left[index_left] <= right[index_right], add left[index_left] to the list and increment index_left
	# 	otherwise if left[index_left] > right[index_right], add right[index_right] and increment index_right
	# if index_right reaches len(right), append the remainder of left starting at index_left and break
	# if index_left reaches len(left), append the remainder of right starting at index_right and break
	# return result
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

def insertion_sort(array):
	# starts at second item, for every i in array, sets j = i - 1 and saves the right_item = array[i]
	# while array[j] is greater than right_item, move the array[j] one position to the right and decrease j by 1
	# then when there are no more greater items, set array[j + 1] to the right_item which is lower than all the moved items
	# insertion sort is faster than bubble sort, O(n^2)
	for i in range(1, len(array)): # starts at item 1 so it can use the left item as j
		j = i - 1
		right_item = array[i] # name it something else so array[j + 1] doesnt overwrite array[i]
		while j >= 0 and array[j] > right_item: # switch item j and the next right item bc left item > right item
			array[j + 1] = array[j]
			j = j - 1
		array[j + 1] = right_item
	return array

# Selection Sort (simple, in-place, not stable)
def selection_sort(a):
	# time best: "O(n²)", time average: "O(n²)", time worst:"O(n²)", space complexity: "O(1)"
    a = list(a)
    n = len(a)
    for i in range(n):
        m = i
        # Find minimum element in remaining unsorted array
        for j in range(i+1, n):
            if a[j] < a[m]:
                m = j
        if m != i:
            # Swap found minimum with first element
            a[i], a[m] = a[m], a[i]
    return a

# Bubble Sort - Simple comparison-based algorithm, Repeatedly steps through the list, compares adjacent elements and swaps them if wrong order
def bubble_sort(self, arr: List[int]) -> List[int]:
    # time best: "O(n)", time average: "O(n²)", time worst:"O(n²)", space complexity: "O(1)"
	arr = arr.copy()  # Don't modify original
	n = len(arr)
	for i in range(n):
		swapped = False
		# Last i elements are already sorted
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		# If no swapping occurred, array is sorted
		if not swapped:
			break
	return arr

def tim_insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return arr

def tim_merge(left, right):
    # If first item of left < first item of right, return a list of [left[0]] + tim_merge(left[1:], right)
    # else return a list of [right[0]] + tim_merge(left, right[1:])
    if left[0] < right[0]:
        # If the first element of the left subarray is smaller, recursively merge the left subarray with the right one
        return [left[0]] + tim_merge(left[1:], right)
    else:
        # If the first element of the right subarray is smaller, recursively merge the right subarray with the left one
        return [right[0]] + tim_merge(left, right[1:])

def tim_sort(arr):
	# set min_run = 32 and n = len(array)
	# for each i in range(0, n, min_run)
	#    apply insertion_sort(array, i, min(i + min_run - 1, n-1))
	# then set size = min_run and while size < n
	# for start in range(0, n, size * 2)
	#     find the mid (start + size 32) and endpoint (min(start + size 32 * 2 - 1, n - 1)) of the left and right subarrays
	#     then merge the subarrays with tim_merge(array[start:mid], array[mid:end + 1])
	#     then assign the merged array to the original array[start:start + len(merged_array)] = merged_array
	# then increase the merge size by multiplying it by 2
	# Timsort sorts the list in place without having to create new arrays like merge sort and Quicksort do
    min_run = 32
    n = len(array)
    # Traverse the array and do insertion sort on each segment of size min_run
    for i in range(0, n, min_run):
        tim_insertion_sort(array, i, min(i + min_run - 1, (n - 1)))
    # Start merging from the size of min_run
    size = min_run
    while size < n:
        # Divide the array into merge size
        for start in range(0, n, size * 2):
            # Find the mid and endpoint of the left and right subarrays
            mid = start + size # start + 32
            end = min((start + size * 2 - 1), (n - 1)) # start + 64 - 1 or n - 1
            # Merge the two subarrays
            merged_array = tim_merge(array[start:mid], array[mid:end + 1])
            # Assign the merged array to the original array
            array[start:start + len(merged_array)] = merged_array
        # Increase the merge size for the next iteration
        size = size * 2
    return array

# linear search doesnt require sorted data, whereas binary search, interpolation search, jump search, and exponential search do require sorted data
# Interpolation Search is effective for large uniformly distributed sorted arrays, O(log n) degrading to O(n), estimates target position based on the key value and range of search space
# Jump search O(√n) jumps a set number of steps (like the root of the list length), then performs linear search on the smaller range once the target is likely within the current block
# For unsorted data, Linear Search is the primary option
# For sorted data, Binary Search is generally the most efficient choice, while Interpolation Search can be faster for uniformly distributed data, and Jump Search offers a good compromise between simplicity and performance.

def linear_search(array, val):
	# O(n)
	# search each item in the array, checking if it equals val and returning the item if so, otherwise return -1
	for i, item in enumerate(array):
		if item == val:
			return i
	return -1

def recursive_linear_search(array, low, high, val):
	# check that left and right are less than the array length
	# if right < left the val was not found so return -1
	# if array[left] or array[right] equals val, return left or right
	# otherwise call search again, with incremented left/right indexes
	if not (0 <= high < len(array) and 0 <= low < len(array)):
		raise Exception("Invalid upper/lower bound")
	if high < low:
		return -1
	if array[low] == val:
		return low
	if array[high] == val:
		return high
	return recursive_linear_search(array, low + 1, high - 1, val)

def binary_search(array, val):
	# O(log n)
	# while left index (starts at 0) is less than or equal to right index (starts at len(array) - 1)
	# finds the midpoint of left and right
	# then compares val to the middle element (left + (right - left) // 2)
	# if array[mid] is val, return mid
	# otherwise increases the left index if array[mid] < val and if array[mid] > val, decreases the right index
	# otherwise return -1
	left = 0
	right = len(array) - 1
	while left <= right:
		mid = left + (right - left) // 2
		if array[mid] == val:
			return mid
		elif array[mid] < val:
			left = mid + 1
		else:
			right = mid - 1
	return -1

def std_lib_binary_search(array, val):
	# bisect.bisect_list to get the index to insert val at, otherwise return -1
	# bisect.insort() to insert val
	index = bisect.bisect_list(array, val)
	if index != len(array) and array[index] == val:
		return index
	return -1

def exponential_search(array, val):
	# if the first item is val, return 0
	# Otherwise start at index 1 and double the index until the left/right search range is found
	# the left index is bound // 2 and the right index is bound * 2 until array[bound] > val
	# then apply Binary Search within that subarray
	if array[0] == val:
		return 0
	# Start at index 1 and double the index until the search range is found.
	bound = 1
	while bound < len(array) and array[bound] < val:
		bound = bound * 2
	left = bound // 2
	right = min(bound, len(array) - 1)
	# If the target is within the range, apply Binary Search within that subarray
	return e_binary_search(array, val, left, right)

def e_binary_search(array, val, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1

vertices: dict[int, list[int]] = {}

def bfs(vertices: dict, start_vertex: int) -> set[int]:
	# add the start vertex to visited, put the start vertex on the queue
	# while not queue.empty(), get the vertex and add it to visited, then add the adjacent vertexes to the queue
	# return visited
	visited = set(start_vertex)
	queue: Queue = Queue()
	queue.put(start_vertex)
	# get the vertex, add the adjacent vertexes
	while not queue.empty():
		vertex = queue.get()
		if vertex not in visited:
			visited.add(vertex)
			for adjacent_vertex in vertices[vertex]:
				queue.put(adjacent_vertex)
	return visited

# dfs - pops last instead of first element, and reverses vertices[vertex]
def dfs(vertices: dict, start_vertex: int) -> set[int]:
	# add the start vertex to visited, put the start vertex on the stack
	# while stack, pop the vertex and add it to visited, then add the reversed adjacent vertexes to the stack
	# return visited
	visited = set(start_vertex)
	stack = []
	stack.append(start_vertex)
	# pop the vertex, add the adjacent vertexes
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			for adjacent_vertex in reversed(vertices[vertex]):
				stack.append(adjacent_vertex)
	return visited
