def permutations(s):
	if len(s) < 2:
		return set(s)

	# Permutations of "abc" is the superset of
	# - "a" + each permutation of "bc"
	# - "b" + each permutation of "ac"
	# - "c" + each permutation of "ab"
	# Thus get permutations recursively of each substring
	return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))

print(permutations("a"))
print(permutations("ab"))
print(permutations("aabb"))
print(permutations("abccd"))