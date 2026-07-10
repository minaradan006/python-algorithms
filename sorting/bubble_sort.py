from typing import List, TypeVar

T = TypeVar('T', int, float, str)

def bubble_sort(arr: List[T]) -> None:
	"""
	Sorts a list of elements in ascending order using the Bubble Sort algorithm.

	Time Complexity:
		- Best Case: O(n) if the list is already sorted
		- Average Case: O(n^2) due to the nested comparison passes.
	Space Complexity: O(1) as it sorts the list in-place

	Args:
		arr (List[T]): A list of comparable elements to be sorted in-place
	Returns:
		None: the list is sorted in-place
	"""
	n: int = len(arr)

	for i in range(n - 1):
		swapped = False

		for j in range(n - 1 - i):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True

		if not swapped:
			break
