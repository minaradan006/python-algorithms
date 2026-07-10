from typing import List, TypeVar

T = TypeVar('T', int, float, str)

def linear_search(arr: List[T], num: T) -> int:
	n: int = len(arr)

	for idx in range(n):
		if arr[idx] == num:
			return idx

	return -1
