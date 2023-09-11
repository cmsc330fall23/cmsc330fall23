def app(f):
  return (f(3))

print(app(lambda x: x + 1))
print(app(lambda x: x * 2))
print(app(lambda x: -x * 2))
print(app(lambda x: x %2==0))

def add1(x):
  return x + 1

print(app(add1))

add = lambda x: (lambda y: x + y)

add3 = add(3)
'''
add3 => (lambda y: x + y),(x:3)
add3(5) : (lambda y: x + y),(x:3,y:5) -> 8

environment: a mapping of variables to values
closure: a tuple of (code to be executed, environment related to that code)

add = function
add3 = {lambda y: x + y,(x:3)}
'''
def f(x):
  return x + 1

def g(x):
  return x * 2

def h(x):
  if x %2==0:
    return f
  return g

print("Ex1")
i = h(2)
j = h(3)
print(i(3))
print(j(3))


def add1(lst):
  ret = []
  for x in lst:
    ret.append(x+1)
  return ret

def x2(lst):
  ret = []
  for x in lst:
    ret.append(x*2)
  return ret

def even(lst):
  ret = []
  for x in lst:
    ret.append(x%2==0)
  return ret

def common(lst,f):
  ret = []
  for x in lst:
    ret.append(f(x))
  return ret

concat(lst):
  ret = ""
  for x in lst:
    ret += x
  return ret
 
sum(lst):
  ret = 0
  for x in lst:
    ret += x
  return ret

prod(lst):
  ret = 1
  for x in lst:
    ret *= x
  return ret

common(lst,init,f):
  ret = init
  for x in lst:
    # ret _ x #updates ret ret = ret OP x
    ret = f(ret,x)
  return ret
f = lambda x,y: x+[y]
reduce(f,[1,2,3,4],[])
f([],1) => [1]

reduce(f,[2,3,4],[1])

