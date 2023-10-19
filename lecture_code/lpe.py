'''
CFG
E -> M + E|M - E|M
M -> N * M|N / M|sq M|N
N -> n|(E)

1 + 2
1+2
1 / 3 * 5
1 * (2 - 4)
12+13
  -> [12], "+13"

terminals: n,+,-,/,*,(,)
'''

from functools import reduce
import re
# string -> token list
def lex(instr):
  toklst = []
  number_re = re.compile(r"^(-?\d+)")
  terminal_re = re.compile(r"^(sq|[()\-+/*])")
  wspace_re = re.compile(r"^(\s+)")
  pos = 0
  strlen = len(instr)
  while pos < strlen:
    match = re.match(number_re,instr[pos:])
    if match:
      toklst.append(match.group(1))
      pos += len(match.group(1))
    else:
      match = re.match(terminal_re,instr[pos:])
      if match:
        toklst.append(match.group(0))
        pos += len(match.group(0))
      else:
        match = re.match(wspace_re,instr[pos:])
        if match:
          pos += len(match.group(1))
        else:
          raise SyntaxError("Invalid character")
  return toklst

class Node:
  def __init__(self,v,t=None,left=None,right=None):
    self.type = t
    self.value = v
    self.left = left
    self.right = right

  def __str__(self):
    ret = str(self.value) 
    if self.left:
      ret += " " + str(self.left)
    if self.right:
      ret += " " + str(self.right)
    return ret

# token list -> tree
def parser(toklst):
  tree,remain = parse_e(toklst)
  if remain == []:
    return tree
  raise SyntaxError("leftover tokens")
  
# token list -> (tree,remaining token list)
def parse_e(toklst):
  mtree,remain = parse_m(toklst)
  if len(remain) > 0 and remain[0] in ["+","-"]:
    etree,new_remain = parse_e(remain[1:]) 
    return Node(remain[0],"op",mtree,etree),new_remain
  return mtree,remain

# token list -> (tree,remaining token list)
def parse_m(toklst):
  if len(toklst) > 0 and toklst[0] == "sq":
    arg,new_remain = parse_m(toklst[1:])
    return Node(toklst[0],"op",arg),new_remain
  ntree,remain = parse_n(toklst)
  if len(remain) > 0 and remain[0] in ["/","*"]:
    mtree,new_remain = parse_m(remain[1:]) 
    return Node(remain[0],"op",ntree,mtree),new_remain
  return ntree,remain

# token list -> (tree,remaining token list)
def parse_n(toklst):
  if len(toklst) > 0:
    fst = toklst[0]
  else:
    raise SyntaxError("Empty")
  if fst == "(":
    etree,remain = parse_e(toklst[1:])
    if len(remain) > 0 and remain[0] == ")":
      return etree,remain[1:]
    else:
      raise SyntaxError("unbalanced parens")
  else:
    try:
      int(fst)  
    except:
      raise SyntaxError("expected a number")  
    return Node(fst),toklst[1:]


# tree -> value
class Node:
  def __init__(self,v,t=None,left=None,right=None):
    self.type = t
    self.value = v
    self.left = left
    self.right = right

def eval(tree):
  if tree.type:
    leftv = eval(tree.left)
    if tree.value == "sq":
      return leftv * leftv
    else:
      rightv = eval(tree.right)
    if tree.value == "+":
      rightv = eval(tree.right)
      return leftv + rightv
    if tree.value == "-":
      return leftv - rightv
    if tree.value == "*":
      return leftv * rightv
    if tree.value == "/":
      return leftv / rightv
  return int(tree.value)


# LEXER

#things that work
assert(lex("1 + 2") == ['1', '+', '2']) 
assert(lex("1+2") == ['1', '+', '2']) 
assert(lex("1 * (3 - 4)") == ['1', '*', '(', '3', '-', '4', ')']) 
assert(lex("1 * 3 - 4)") == ['1', '*', '3', '-', '4', ')'])
assert(lex("1 * (3 - 4") == ['1', '*', '(', '3', '-', '4'])
assert(lex("+ 1 2") == ['+', '1', '2'])
assert(lex("") == [])
assert(lex("-3") == ['-3'])
assert(lex("- 3") == ['-','3'])
assert(lex("1-3") == ['1', '-3'])
assert(lex("sq 2") == ['sq', '2'])

# things that shouldn't work
try:
  (lex("a")) 
except SyntaxError:
  assert(True)
except:
  assert(False)
try:
  (lex("1 + ?3")) 
except SyntaxError:
  assert(True)
except:
  assert(False)

# PARSER
assert(str(parser(lex("1 + 2"))) == "+ 1 2")
assert(str(parser(lex("1 + 2 - 3"))) == "+ 1 - 2 3")
assert(str(parser(lex("1 * 2 - 3"))) == "- * 1 2 3")
assert(str(parser(lex("1 * (2 - 3)"))) == "* 1 - 2 3")
assert(str(parser(lex("(2 + (3 - 2)) + 1"))) == "+ + 2 - 3 2 1")
assert(str(parser(lex("2"))) == "2")
assert(str(parser(lex("sq 2"))) == "sq 2")

#things that should not work
try:
  parser(lex("1 * (2 - 3)")) 
except SyntaxError:
  assert(True)
except:
  assert(False)
try:
  (parser(lex("1 * + 2")))
except SyntaxError:
  assert(True)
except:
  assert(False)
try:
  (parser(lex("()")))
except SyntaxError:
  assert(True)
except:
  assert(False)
try:
  (parser(lex("1 * + 2")))
except SyntaxError:
  assert(True)
except:
  assert(False)

# EVAL
assert(eval(parser(lex("4 + 2")))==6)
assert(eval(parser(lex("4 * 2")))==8)
assert(eval(parser(lex("4 / 2")))==2.0)
assert(eval(parser(lex("4 - 2")))==2)
assert(eval(parser(lex("4 * (2 - 3)")))==-4)
assert(eval(parser(lex("4 * 2 - -3")))==11)
assert(eval(parser(lex("1 + sq 2")))==5)
