from functools import reduce

def is_present(x, lst):
    return reduce(lambda acc, el: acc or el == x, lst, False)

def count_occ(x, lst):
    return reduce(lambda acc, el: acc + 1 if el == x else acc, lst, 0)

def count_occ_2d(x, matrix):
    return reduce(lambda acc, row: acc + count_occ(x, row), matrix, 0)