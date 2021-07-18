# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
	return sum_of_multiples(number, 3) + sum_of_multiples(number, 5) - sum_of_multiples(number, 15)
	
def sum_of_multiples(number, base):
	n = int((number - 1) / base)
	return (n + 1) * n / 2 * base;