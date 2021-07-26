import functools

def find_it(seq):
    return functools.reduce(lambda a, b: a ^ b, seq)