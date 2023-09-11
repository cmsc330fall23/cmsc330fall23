a = 5
b = 20
def h(a):
  d = True
  e = 0
  while d:
    if a < b - a:
      a = a + 1
      e = e + 1
    else:
      d = False
  return e
 
f = input("Enter a number: ")
print(h(int(f)) + a)
