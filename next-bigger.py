def next_bigger(n):
	digits = []

	# Push digits into list until a decreased value is found
	while len(digits) < 2 or digits[-2] <= digits[-1]:
		# If no decrease is found when all digits are pushed, return failure
		if n == 0:
			return None
		digits.append(n % 10)
		n = int(n / 10)

	# The last digit in list is the decreased digit, i.e. the digit needs to be replaced
	target = digits[-1]
	digits.sort()

	# Find the smallest digit that is bigger than the target digit
	for d in digits:
		if d > target:
			digits.remove(d)
			# Push this digit back to the tail of the number, so it replaces the previous digit
			n = n * 10 + d
			break

	# Push the remaining digits back to the number
	for d in digits:
		n = n * 10 + d

	return n

print(next_bigger(12))