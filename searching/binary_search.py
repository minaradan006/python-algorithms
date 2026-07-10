from typing import List, Tuple, Optional

def binary_search(search_list: List[int], value: int) -> Tuple[int, List[int]]:
	"""
	Performs a binary search on a sorted list to find the target value,
	tracking the sequence of midpoints visited during the search.

	Time Complexity: O(log n)
	Space Complexity: O(log n) due to path tracking

	Args:
		search_list (List[int]): A sorted list of integers to search.
		value (int): The target integer to find.

	Returns:
		Tuple[int, List[int]]:
			- The index of the value if found, or -1 if not found.
			- A list of values checked along the path to the target.
	"""
	path_to_target: List[int] = []
	low: int = 0
	high: int = len(search_list) - 1

	while low <= high:
		mid: int = (low + high) // 2
		value_at_middle: int = search_list[mid]
		path_to_target.append(value_at_middle)

		if value == value_at_middle:
			return mid, path_to_target
		elif value > value_at_middle:
			low = mid + 1
		else:
			high = mid - 1

	return -1, path_to_target
