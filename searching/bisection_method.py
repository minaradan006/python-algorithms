def square_root_bisection(num: float, tol: float = 1e-5, max_iter: int = 100) -> float | None:
	"""
	Calculates the approximare square root of a non-negative number using
	the continuous Bisection Method.

	Time Complexity: O(log((high - low) / tol))
	Space Complexity: O(1)

	Args:
		num (float): The number to find the square root of.
		tol (float): The convergence tolerance for the interval width.
		max_iter (int): The maximum number of iterations allowed.

	Returns:
		float | None: The approximate square root, or None if num is negative.
	"""
	if num < 0:
		return None

	low: float = 0.0
	high: float = max(1.0, num)
	iters: int = 0

	while (high - low) > tol and iters < max_iter:
		mid: float = (low + high) / 2.0

		if mid ** 2 > num:
			high = mid
		else:
			low = mid

		iters += 1

	return mid
