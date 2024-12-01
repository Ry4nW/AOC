data = [x.rstrip() for x in open("input.txt").readlines()]

print(sum(abs(int(t[0]) - int(t[1])) for t in zip(*map(sorted, zip(*map(str.split, data))))))
