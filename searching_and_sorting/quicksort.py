from typing import List, TypeVar
import random

T = TypeVar('T', int, float, str)

def quick_sort_readable(numbers: List[T]) -> List[T]:
	"""
	Sorts a list of elements in ascending order using an out-of place Quicksort.
	High readability, but higher memory usage.

	Time Complexity:
		- Best/Average Case: O(n log n)
		- Worst Case: O(n^2) when pivot choices are highly unbalanced.
	Space Complexity:
		- Average Case: O(n log n) due to allocating new sub-lists and call
						stack overhead.

	Args:
		numbers (List[T]): A list of comparable elements.

	Returns:
		List[T]: A new list containing the sorted elements.
	"""
	if len(numbers) <= 1:
		return numbers
	
	pivot = random.choice(numbers)

	less_than_pivot = [x for x in numbers if x < pivot]
	equal_to_pivot = [x for x in numbers if x == pivot]
	greater_than_pivot = [x for x in numbers if x > pivot]

	return quick_sort_readable(less_than_pivot) + equal_to_pivot + quick_sort_readable(greater_than_pivot)


def quick_sort_inplace(numbers: List[T]) -> None:
	"""
	Sorts a list in-place using Lomuto's partitioning.
	Optimized for memory efficiency.

	Time Complexity:
		- Best/Average Case: O(n log n)
		- Worst Case: O(n^2) when pivot choices are highly unbalanced.
	Space Complexity: O(log n) auxiliary space for recursive stack.

	Args:
		numbers (List[T]): A list of comparable elements.
	Returns:
		None: Modifies the input list directly.
	"""
	def _quicksort(arr: List[T], low: int, high: int):
		if low < high:
			pivot_idx = _partition(arr, low, high)
			_quicksort(arr, low, pivot_idx - 1)
			_quicksort(arr, pivot_idx + 1, high)

	def _partition(arr: List[T], low: int, high: int) -> int:
		rand_idx: int = random.randint(low, high)

		arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

		pivot = arr[high]
		i = low - 1

		for j in range(low, high):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]

		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		return i + 1

	_quicksort(numbers, 0, len(numbers) - 1)
