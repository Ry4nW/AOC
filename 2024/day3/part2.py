data = [x.rstrip() for x in open("input.txt").readlines()]

import re

r = 0
on = True
for l in data:
  ops = re.findall(r'mul\([0-9][0-9]*[0-9]*,[0-9][0-9]*[0-9]*\)|do\(\)|don\'t\(\)', l)
  
  for op in ops:
    if op[:3] == "do(": 
      on=True 
      continue
    elif op[:3] == "don": 
      on=False
      continue
    if not on: continue
    f,s = op.split(',')
    f = f.split('(')
    s = s.split(')')
    
    r += int(f[-1]) * int(s[0])

print(r)
