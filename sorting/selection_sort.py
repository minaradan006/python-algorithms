from typing import List, TypeVar

T = TypeVar('T', int, float, str)

def selection_sort(numbers: List[T]) -> None:
	"""
	Sorts a list of elements in ascending order using the Selection Sort
	algorithm.

	Time Complexity: O(n^2) due to the nested loops scanning
	Space Complexity: O(1) as it sorts the list in-place

	Args:
		numbers (List[T]): A list of comparable elements to be sorted.
	Returns:
		None: The list is sorted in-place
	"""
	n: int = len(numbers)
	for i in range(n):
		min_index: int = i

		for j in range(i + 1, n):
			if numbers[j] < numbers[min_index]:
				min_index = j

		if min_index != i:
			numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

	return numbers
