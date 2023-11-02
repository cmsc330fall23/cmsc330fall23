from functools import reduce
import re

'''
link to lolcode: http://www.lolcode.org/
Source: https://github.com/justinmeza/lci
Spec (1.2): https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md
'''

'''
n (number)
x (variable)
SUM OF x AN y (addition)
I HAS A x ITZ y \n (variable binding)
'''

def lexer(instr):
  def lex(lolcode,toks):
    if len(lolcode) == 0:
      return toks
    var_re = re.compile(r"^[a-z0-9]+")
    number_re = re.compile(r"^(-?\d+)")
    terminal_re = re.compile("^(SUM|OF|AN|ITZ|HAS|\n)")
    terminal2_re = re.compile("^(I|A)")
    match = number_re.match(lolcode)
    if match:
      group = match.group(0)
      return lex(lolcode[len(group):],toks+[["NUMBER",int(group)]])
    match = var_re.match(lolcode)
    if match:
      group = match.group(0)
      return lex(lolcode[len(group):],toks+[["VAR",group]])
    match = terminal_re.match(lolcode)
    if match:
      group = match.group(0)
      return lex(lolcode[len(group):],toks+[group])
    match = terminal2_re.match(lolcode)
    if match:
      group = match.group(0)
      return lex(lolcode[len(group):],toks+[group])
    return lex(lolcode[1:],toks) #ignore bas symbols
  return lex(instr,[])


class Var:
  def __init__(self,v):
    self.value = v

  def __str__(self):
    return ("Var("+str(self.value)+")")

class Num:
  def __init__(self,v):
    self.value = v

  def __str__(self):
    return ("Num("+str(self.value)+")")
  
class Sum:
  def __init__(self,x,y):
    self.left= x
    self.right=y

  def __str__(self):
    return ("SUM("+str(self.left)+","+str(self.right)+")")

class Has:
  def __init__(self,x,y,z):
    self.var= x
    self.val=y
    self.body=z

  def __str__(self):
    return ("HAS("+str(self.var)+","+str(self.val)+","+str(self.body)+")")

'''
E -> x|n|I HAS A x ITZ E\nE|SUM OF E AN E
'''
# token list -> tree
def parser(toklst):
  def parse(toks):
    if toks == []:
      raise SyntaxError("Empty Tokens")
    if type(toks[0]) == list:
      if toks[0][0] == 'NUMBER':
        return Num(toks[0][1]),toks[1:]
      else: 
        return Var(toks[0][1]),toks[1:]
    if toks[0] == "SUM" and toks[1] == "OF":
      ltree,left = parse(toks[2:])
      if left[0] == "AN":
        rtree,left = parse(left[1:])
        return Sum(ltree,rtree),left
      else:
        raise SyntaxError("Missing AN")
    if toks[0]=="I" and toks[1] == "HAS" and toks[2] == "A":
      if type(toks[3]) == list and toks[3][0] == "VAR":
        var_name = toks[3][1]
        if toks[4] == "ITZ":
          val,left = parse(toks[5:])
          if left[0]=="\n":
            bod,left = parse(left[1:])
            return Has(var_name,val,bod),left
          else:
            raise SyntaxError("Needed newline")
        else:
          raise SyntaxError("Missing ITZ")
      raise SyntaxError("Expecting variable nae")
  tree,left = parse(toklst)
  if left == []:
    return tree
  raise SyntaxError("leftover tokens")


def lookup(x,e):
  if e == []:
    raise Exception("unbound var")
  if e[0][0] == x:
    return e[0][1]
  else:
    return lookup(x,e[1:])

'''
--------
A;n => n


A(x) = v
--------
A;x => v

A;e1 => v1    A;e2 => v2    v3 is v1 + v2
-----------------------------------------
      A;SUM OF e1 AN e2 => v3

A;e1 => v1     A,var:v1;e2 => v2
--------------------------------
 A;I HAS A var ITZ e1\ne2 => v2

'''

def interp(tree,env):
  if type(tree) == Num:
    return tree.value
  if type(tree) == Var:
    return lookup(tree.value,env)
  if type(tree) == Has:
    val = interp(tree.val,env)
    new_env  = [(tree.var,val)]+env
    return interp(tree.body,new_env)
  if type(tree) == Sum:
    left =  interp(tree.left,env)
    right = interp(tree.right,env)
    return left + right

print(lexer("3"))
print(lexer("I HAS A x ITZ 3\nx"))
print(lexer("SUM OF 4 AN 3"))
print(lexer("x"))
print(lexer("res2"))

print(parser(lexer("3")))
print(parser(lexer("I HAS A x ITZ 3\nx")))
print(parser(lexer("SUM OF 4 AN 3")))
print(parser(lexer("x")))
print(parser(lexer("res2")))

print(interp(parser(lexer("3")),[]))
print(interp(parser(lexer("I HAS A x ITZ 3\nx")),[]))
print(interp(parser(lexer("I HAS A x ITZ 3\n5")),[]))
print(interp(parser(lexer("I HAS A x ITZ 5\nx")),[]))
print(interp(parser(lexer("SUM OF 4 AN 3")),[]))
print(interp(parser(lexer("SUM OF 4 AN 6")),[]))
print(interp(parser(lexer("I HAS A x ITZ 5\nSUM OF x AN 4")),[]))
print(interp(parser(lexer("I HAS A x ITZ 5\nSUM OF 6 AN x")),[]))
print(interp(parser(lexer("I HAS A x ITZ 5\nI HAS A y ITZ 7\nSUM OF y AN x")),[]))
print(interp(parser(lexer("I HAS A x ITZ 5\nI HAS A y ITZ 7\nSUM OF x AN y")),[]))
print(interp(parser(lexer("I HAS A x ITZ 5\nI HAS A x ITZ 7\nSUM OF x AN x")),[]))
