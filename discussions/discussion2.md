# Discussion 2

## Reminders

- Project 1 due **Sunday, September 10** at **11:59 PM**
- Quiz 1 is next week (**Friday, September 15th**) **during discussion**

## Lambdas

Lambdas are anonymous functions that can take any number of arguments but can only contain a single expression. They have many use cases which include:

- passing into higher order functions like map and reduce
- passing in as a key for `filter()` and `sorted()`

```python
# basic example
plus_one = lambda x : x + 1
plus_one(5) # returns 6

# sort a dictionary based on value
d = {"a": 4, "b": 1, "c": 7}
dict(sorted(d.items(), key=lambda x : x[1])) # returns {'b': 1, 'a': 4, 'c': 7}
```

## Map

```python
# map with lambda
list(map(lambda x : x * 2, [1,2,3,4])) # outputs [2,4,6,8]
```

Map applies a function to every element of an iterable (list, tuple, etc.) This can either be a predefined function or a lambda 

Note that map returns a map object, which you’ll need to convert to a list to print

## Reduce

```python
lst = [1,2,3,4,5]
reduce(lambda a,b : a+b, lst, 0) # sums up the elements (15)
# note that the last argument is the 'initializer' - 
# if unspecified, the first element of the iterable will be used as the initializer 
```

Reduce applies a function to all elements in the iterable and returns an “accumulation” of sorts.

## Partial Application (Currying)

Partial application is a process of fixing a certain number of arguments in a function.

There are a few ways of doing this in python, here’s examples using lambdas as well as [functools](https://docs.python.org/3/library/functools.html).

```python
# lambdas go brr
add = lambda a : lambda b : a + b

# partially apply add with the first number
add3 = add(3) # returns a function looking something like lambda b : 3 + b

add3(4) # returns 7 (3 + 4)

# another similar example
printMsg = lambda header : lambda msg : f'{header} {msg}'

printDebug = printMsg("[DEBUG]")

printDebug("failed") # returns "[DEBUG] failed"
```

```python
# this behavior is not implemented by default so import it
from functools import partial

def addNums(a,b):
	return a + b

# here, we fix the first positional argument in addNums to be 3, 
# and use the resultant function
add3 = partial(addNums, 3)

add3(4) # returns 7

# this behavior also works with keyword arguments like so:

# here we have a partial int function with the base fixed to 16
# this converts a base 16 (hex) string to an int
hexToInt = partial(int, base=16)

hexToInt("DEADBEEF") # returns 3735928559
```

## Closure

A closure is a way to create/bind something called a context or environment

```python
x = 5
a = lambda y : x + y # x=5, closure created, but x can change
print(a(5)) # prints 10
x = 3
print(a(5)) # prints 8

sub = lambda x :lambda y : x - y
x=3
subfrom3 = sub(x) # x=3, closure created, only uses 3 as x
print(subfrom3(5)) # prints -2
x=5 # will not affect subfrom3, because x was 3 when subfrom3 was defined
print(subfrom3(5)) # still -2
```

This is because in Python, the variable lookup is done when the closure is called. Note in  `a = lambda y : x + y`, x is not bound locally while in  `sub = lambda x :lambda y : x - y` is bound locally.

## Regular Expressions

Regular expressions are patterns that are used to match strings and extract information. They are internally implemented using finite state automata, which will be covered later in the class. For now, we will focus on Regular Expressions in Python.

The simplest Regex matches a string literal:

```python
import re

pattern = r"world" # use r to indicate that this is a raw string
string = "hello world"

if re.findall(pattern, string):
	print("we found it!")
```

There are several Python functions we can use to work with regex. The following is not a comprehensive list. Please refer to the [documentation](https://docs.python.org/3/library/re.html) for the `re` module for more details.

### `re.findall(pattern, string):`

Returns a list containing all of the matches, or an empty list if none are found

```python
matches = re.findall(r"cmsc3[0-9]*", "cmsc216 cmsc250 cmsc330 cmsc351 cmsc451")
matches # ['cmsc330', 'cmsc351']
matches = re.findall(r"cmsc1[0-9]*", "cmsc216 cmsc250 cmsc330 cmsc351 cmsc451")
matches # []
```

### `re.search(pattern, string):`

Returns a `Match` object if a match is found, or `None` otherwise. If there is more than one match, only the first occurrence will be returned.

```python
match = re.search(r"hello", "hello world")
span = match.span() # returns a tuple containing start and end position of match
string = match.string # returns the string passed in
group = match.group() # returns the part of the string where the match was found
```

Note that if you want to repeat a pattern, you can use `re.compile` to be more efficient:

```python
pattern = re.compile("hello")
string = "hello world"
if pattern.findall(string):
	print("we found it!")
```

Aside from string literals, there are many more patterns that regex can describe:

- Ranges: `/[a-z]/`, `/[c-k]/`, `/[A-Z]/`, `/[0-9]/` We use these ranges, also known as character classes, to accept characters within a specified range (inclusive).
- Or (Union): `/a|b|c/` We use this to accept one character from the given choices.
- Sets: `/[abc]/`, `/[34567]/` The bracket notation is shorthand for the union operation on the characters within the brackets;
- Meta Characters: `/\d/`, `/\D/`, `/\s/` We use these characters to match on any of a particular type of pattern.
- Wildcard: `.` We use this to match on any character. Note: to use a literal `.`, we must escape it, i.e. `/\./`.
- Beginning of pattern: `/^hello/` Here, the string must begin with "hello".
- End of pattern: `/hello$/` Here, the string must end with "hello".
- Beginning and end of pattern: `/^abc$/` We will use this to match exactly to patterns, so any string matching the above Regex must only have “abc” from start to end
- Repetitions: `/a*/`, `/a+/`, `/a?/`, `/a{3}/`, `/a{4,6}/`, `/a{4,}/`, `/a{,4}/` We use these to describe when a pattern is to be repeated. Note that the repetition only occurs on the character immediately preceding it; to repeat a whole pattern, use parentheses
- Negation: `/[^a-z]/`, `/[^0-9]/` We use these to exclude a range of characters.

### Question:

Can every string pattern be expressed with a regex?

**Answer: No!**

There are certain string patterns that ************cannot************ be expressed with regular expressions. This is because regular expressions are “memoryless”; they cannot keep track of what they have already seen.

As an example, consider the following (incorrect) regex for phone numbers with optional “()” symbols:

`(?\d{3})?\d{4}-\d{4}`

This regular expression will erroneously match strings like the following:

`(123-1234-1234`

`123)-1234-1234`

The fundamental issue is that regex cannot “know" whether it has seen a `(` when it checks for the `)`. In general, it is impossible to write a regex to match strings with balanced parentheses or similar.

## Python HOF Exercises

> **NOTE:** You must use `reduce()` and lambdas for the exercises below. 

To import the reduce function, put `from functools import reduce` at the beginning of your file.
> 

### `is_present(x, lst):`

Takes in a list `lst` and a value `x` and returns `True` if `x` is present in `lst`, `False` otherwise.

```python
is_present(5, [1, 2, 3, 4, 5]) == True
is_present(-1, [0, -3, 7, 9]) == False
```

### `count_occ(x, lst):`

Takes in a list `lst` and a value `x` and returns the number of times `x` appears in `lst` .

```python
count_occ(1, [2, 1, 1, 0, 3]) == 2
count_occ(5, [1, 2, 3, 4]) == 0
count_occ("apple", ["apple", "banana", "strawberry", "apple"]) == 2
```

### `count_occ_2d(x, matrix):`

Takes in a 2D matrix `matrix` and a value `x` and returns the number of times `x` appears in `matrix`.

```python
count_occ_2d(0, [[1, 1, 0], [0, 1, 0], [1, 1, 0]]) == 4
count_occ_2d(2, [[1, 2, 2], [5, 5, 6], [7, 2, 9]]) == 3
```

## Regex Exercises

Write a regex pattern for each of the following scenarios (or explain why you cannot):

- Alternates between capital & lowercase letters
- Contains an even number of vowels
- Has more 7s, 8s, and 9s than 1s, 2s, and 3s

## Additional Resources

[https://regexr.com/](https://regexr.com/)

[regex101: build, test, and debug regex](https://regex101.com/)

[re — Regular expression operations](https://docs.python.org/3/library/re.html)
