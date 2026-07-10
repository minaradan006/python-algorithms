from typing import List, TypeVar

T = TypeVar('T', int, float, str)

def merge_sort(array: List[T]) -> None:
	"""
	Sorts a list of elements in ascending order using the Merge Sort algorithm.

	Time Complexity: O(n log n) because the array is split evenly into logarithmic
					 layers and reconstructed linearly.
	Space Complexity: O(n) auxiliary space due to slicing operations and temporary
					  subarrays allocated during the merge process.

	Args:
		array (List[T]): A list of comparable elements to be sorted in-place.
	Returns:
		None: List sorted in-place
	"""
	if len(array) <= 1:
		return

	middle_point = len(array) // 2
	left_part = array[:middle_point]
	right_part = array[middle_point:]

	merge_sort(left_part)
	merge_sort(right_part)

	left_idx, right_idx, sorted_idx = 0

	while left_idx < len(left_part) and right_idx < len(right_part):
		if left_part[left_idx] <= right_part[right_idx]:
			array[sorted_idx] = left_part[left_idx]
			left_idx += 1
		else:
			array[sorted_idx] = right_part[right_idx]
			right_idx += 1
		sorted_idx += 1

	while left_idx < len(left_part):
		array[sorted_idx] = left_part[left_idx]
		left_idx += 1
		sorted_idx += 1

	while right_idx < len(right_part):
		array[sorted_idx] = right_part[right_idx]
		right_idx += 1
		sorted_idx += 1
