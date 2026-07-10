from typing import Dict

def fibonacci(n: int, memo: Dict[int, int] = None) -> int:
	"""
	Calculates the nth Fibonacci number using optimized recursive memoization.

	Time Complexity: O(n)
	Space Complexity: O(n)

	Args:
		n (int): The position in the Fibonacci Sequence to calculate.
		memo (Dict[int, int]): A dictionary used as a lookup cache to store
							   previously calculated Fibonacci numbers.
	Returns:
		int: The nth Fibonacci number.
	"""
	if memo is None:
		memo = {}

	if n <= 0: return 0
	if n == 1: return 1

	if n in memo:
		return memo[n]
	
	memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
	return memo[n]
