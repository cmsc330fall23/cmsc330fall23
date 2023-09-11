add1 = lambda x: x + 1
x2 = lambda x: x + x
is_even = lambda x: x%2 == 0
lst = [1,2,3]
list(map(add1,lst))
list(map(x2,lst))
list(map(is_even,lst))
fs = [add1,x2,(lambda x: -x)]
print(list(map(lambda f: list(map(f,lst)),fs)))
print(list(map(lambda f: map(f,lst),fs)))
