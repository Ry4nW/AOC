data = [x.rstrip() for x in open("input.txt").readlines()]

import re

r = 0
on = True
for l in data:
  ops = re.findall(r'mul\([0-9][0-9]*[0-9]*,[0-9][0-9]*[0-9]*\)', l)
  
  for op in ops:
    f,s = op.split(',')
    f = f.split('(')
    s = s.split(')')
    
    r += int(f[-1]) * int(s[0])

print(r)
