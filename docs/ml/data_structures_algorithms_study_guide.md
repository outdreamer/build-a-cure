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
	- graphs

- algorithms

	- sorting algorithms
		- quick sort
		- merge sort
		- tim sort
		- bubble sort

	- search algorithms
		- linear search
		- binary search

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
https://www.geeksforgeeks.org/dsa/top-100-data-structure-and-algorithms-dsa-interview-questions-topic-wise/#
https://medium.com/@contactomyna/python-data-structures-and-algorithms-cheat-sheet-a0e23796dd96