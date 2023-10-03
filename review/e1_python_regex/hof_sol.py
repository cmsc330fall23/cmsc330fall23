from functools import reduce

def most_freq_char(s):
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    return max(freq.items(), key=lambda x: x[1])[0]

def my_hof(lst):
    return reduce(lambda a,h: [h[1]] + a if len(str(h[1])) <= 2 else a, lst, [])

def is_same(lst1,lst2):
	return map(lambda x: True if x[0] == x[1] else False, zip(lst1,lst2))

def most_freq(lst, c):
    return reduce(lambda a, s: (
        a[0] + 1 if most_freq_char(s) == c else a[0], 
        a[1] + len(s) if most_freq_char(s) == c else a[1]
    ), lst, (0, 0))

print(most_freq(["aaa", "bbbc", "aaabbc", "abbcccc"], "a"))
# (2, 9)

print(most_freq_char("aaabbbbc"))