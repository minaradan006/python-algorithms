from typing import List, TypeVar

T = TypeVar('T', int, float, str)

def linear_search(arr: List[T], elem: T) -> int:
	"""
	Searches for a target element within a list sequentially.

	Time Complexity: O(n)
	Space Complexity: O(1)

	Args:
		arr (List[T]): A list of elements to search through
		elem (T): The target element to locate.
	Returns:
		int: The index of the element if found, otherwise -1.
	"""
	n: int = len(arr)

	for idx in range(n):
		if arr[idx] == elem:
			return idx

	return -1
