a = 5

def f():
  a = 4
  global a
  a = a + 1
  print(a)

f()
