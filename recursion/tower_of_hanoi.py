def hanoi_solver(n: int) -> None:
	"""
	Solves the Tower of Hanoi puzzle recursively and prints the steps.

	Time Complexity: O(2^n) because the number of moves doubles with each
					 additional disk.
	Space Complexity: O(n) auxiliary space due to the recursive call stack.

	Args:
		n (int): The number of disks to move.
	Returns:
		None: prints the steps.
	"""
	rods = {
		'A': list(range(n, 0, -1)),
		'B': [],
		'C': []
	}

	def print_state() -> None:
		print(f"A: {rods['A']}   B: {rods['B']}   C: {rods['C']}")

	def move_disks(disks, source, target, auxiliary):
		if disks == 1:
			disk = rods[source].pop()
			rods[target].append(disk)
			print_state()
			return

		move_disks(disks - 1, source, auxiliary, target)

		disk = rods[source].pop()
		rods[target].append(disk)
		print_state()

		move_disks(disks - 1, auxiliary, target, source)

	if n > 0:
		print("Initial State:")
		print_state()
		print("-" * 30)
		move_disks(n, 'A', 'C', 'B')

hanoi_solver(4)