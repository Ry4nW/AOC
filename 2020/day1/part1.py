data = [int(x.rstrip()) for x in open("input.txt").readlines()]

for i in range(len(data)):
  for j in range(i + 1, len(data)):
    n1 = data[i]; n2 = data[j]
    c = n1 + n2
    for k in range(j + 1, len(data)):
      if c + data[k] == 2020:
        print(n1 * n2 * data[k])
