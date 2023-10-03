# Exam 1 Review Session - Python Basics, HOFs, Regex

> Monday, October 2nd

remember to import reduce :\)

```python
from functools import reduce
```

## Python HOFs

### `def most_freq_char(s):`

`str -> str`

Takes in a string `s` and returns the most frequent character that shows up in it

```python
assert most_freq_char("aaabbbbc") == "b"
```

### `def most_freq(lst, c):`

`str[] -> str -> (int, int)`

Takes in a list of strings `lst` and character `c`, returns a tuple where the first element is the number of strings in `lst` that have the most frequent character == c, and the second element is the sum of lengths of these strings

```python
assert most_freq(["aaa", "bbbc", "aaabbc", "abbcccc"], "a") == (2, 9)
# 2 strings match: ["aaa", "aaabbc"]
# len("aaa") + len("aaabbc") = 3 + 6 = 9
```

### `def my_hof(lst):`

Given a list of tuples of integers that are size 3 write a function using reduce that returns all 2nd elements of a tuple that has less than or equal to 2 digits.

### `def is_same(lst1, lst2):`

Given 2 lists,lst1 and lst2, use map to return a list of booleans where index i is true if lst1[i] is equal to lst2[i]. Hint: use zip
