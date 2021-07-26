import operator
import functools

def find_it(seq):
    return functools.reduce(operator.xor, seq)