'''
CFG
E -> M + E|M - E|M
M -> N * M|N / M|N
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
  terminal_re = re.compile(r"^[()\-+/*]")
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
        pos += 1
      else:
        match = re.match(wspace_re,instr[pos:])
        if match:
          pos += len(match.group(1))
        else:
          raise SyntaxError("Invalid character")
  return toklst

# token list -> tree
def parse(toklst):

# tree -> value
def eval(tree):
