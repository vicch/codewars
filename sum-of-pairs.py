# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints, s):
	iset = set()
	for i in ints:
		if (s - i) in iset:
			return [s - i, i]
		iset.add(i)
	return None