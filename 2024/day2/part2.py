data = [x.rstrip() for x in open("input.txt").readlines()]

def safe(l):
  sc = sorted(l)
  rsc = sc.copy()
  rsc.reverse()
  if not (sc == l or rsc == l): return False
  for i in range(1, len(l)):
    dif = abs(l[i] - l[i - 1])
    if not (1 <= dif and dif <= 3): return False
  return True

r = 0
for l in data:
  c = list(map(int, l.split(' ')))
  for i in range(len(c)):
    if safe(c) or safe(c[:i]+ c[i+1:]): r += 1; break
    
print(r)
