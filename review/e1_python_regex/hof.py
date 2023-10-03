from functools import reduce

# Calculates and returns the most frequent character that shows up in string s
# str -> str
def most_freq_char(s):
    freq = {}
    for e in s:
        if e not in freq:
            freq[e] = 1
        else:
            freq[e] += 1

    return sorted(freq.items(), key=lambda x: x[1])[-1][0]
    # reduce(lambda acc, e: )

assert most_freq_char("aaabbbbc") == "b"

# Takes in a list of strings `lst` and character `c`, returns a tuple 
# where the first element is the number of strings in lst that
# have the most frequent character == c, and the second element is the
# sum of lengths of these strings
# str[] -> str -> (int, int)
def most_freq(lst, c):
    return reduce(lambda acc, x: (
        acc[0] + 1 if most_freq_char(x) == c else acc[0],
        acc[1] + len(x) if most_freq_char(x) == c else acc[1]
    ), lst, (0, 0))

# acc = (0, 0), acc[0] = 0, x = "aaa"
# acc = (1, ?), acc[0] = 1, x = "bbbc"
# acc = (1, ?)
# 

assert most_freq(["aaa", "bbbc", "aaabbc", "abbcccc"], "a") == (2, 9)



# Given a list of tuples of integers that are size 3 
# write a function using reduce that returns all 2nd elements of a 
# tuple that has less than or equal to 2 digits.
def my_hof(lst):
    reduce(lambda acc, x: acc + [x[1]] if x[1] <= 99 else acc, lst, [])
    pass

#Given a list of integers remove the dupilcates using reduce
def del_duplicates(lst):
    reduce(lambda acc,x: acc if x in acc else acc + [x] ,lst, [])

# lst=  (1, 2, 3), (3, 24, 5), (5, 2222, 9)
# acc = [], x = (1,2,3), acc + [x[1]] = [] + [2]
# acc = [2], x = (3, 24, 5)
# acc = [2, 24], x = (5, 2222, 9)
# acc = [2, 24]

# Given 2 lists,lst1 and lst2,  use map to return a list of booleans 
# where index i is true if lst1[i] is equal to lst2[i]. Hint: use zip
def is_same(lst1, lst2):
    return list(map(lambda x : lst1[x] == lst2[x], list(range(len(lst1)))))
	return list(map(lambda x: x[0] == x[1] ,zip(lst1,lst2)))


def my_filter(f, lst):
    return reduce(lambda acc, x: acc + [x] if f(x) is True else acc, lst, [])

# my_filter(lambda x: x > 4, [1,2,3,4,5,6])
# acc = [], x = 1, f(x) = False
# acc = [], x = 2, f(x) = False
# acc = [], x = 3, f(x) = False
# acc = [], x = 4, f(x) = False
# acc = [], x = 5, f(x) = True, 5 > 4
# acc = [5], x = 6, f(x) = True, 6 > 4
# acc = [5, 6]
    

#[1,2,3]
#[4,5,6]
#[(1,4),(2,5),(3,6)]
